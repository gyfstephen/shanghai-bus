# coding=utf-8

import json

import redis
import base64

import requests
from bs4 import BeautifulSoup

from settings import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, SID_TTL, STATIONS_TTL, STOPS_TTL

headers = {'User-Agent': 'MicroMessenger/7.0.1380(0x27000034) Process/tools NetType/WIFI Language/zh_CN'}


class RedisClient(object):
    def __init__(self):
        if not REDIS_PASSWORD:
            self.pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        else:
            self.pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD,
                                             decode_responses=True)
        self.client = redis.Redis(connection_pool=self.pool)


client = RedisClient().client


class StopType(object):
    # 上行为0
    # 下行为1
    Up = 0
    Down = 1


class StopInfo(object):
    # 停站信息
    def __init__(self, stop_id, station_name, error=0, terminal='', stopdis=0, distance=0, time=0, **kwargs):
        self.stop_id = int(stop_id)  # 站台id
        self.station_name = station_name  # 站台名称
        self.error = int(error)  # 错误信息 -2=等待发车
        self.plate = terminal  # 车牌信息
        self.stop_dis = int(stopdis)  # 距离当前站台还有X站
        self.distance = int(distance)  # 距离当前站台还有X米
        self.time = int(time)  # 距离当前站台还有X秒

    def dumps(self):
        # 导出数据
        res = {'error': self.error, 'stop_id': self.stop_id, 'station_name': self.station_name, 'plate': self.plate,
               'stop_dis': self.stop_dis, 'distance': self.distance, 'time': self.time}
        return res


class Bus(object):
    def __init__(self, number, stop_type):
        self.number = u'{0}路'.format(number)  # 线路
        self.stop_type = stop_type  # 上行/下行
        self.stations, self.stops = dict(), list()
        self.session = requests.Session()
        self.sid_url = 'https://shanghaicity.openservice.kankanews.com/public/bus/get'
        self.station_url = 'https://shanghaicity.openservice.kankanews.com/public/bus/mes/sid/{0}?stoptype={1}'
        self.stop_url = 'https://shanghaicity.openservice.kankanews.com/public/bus/Getstop'
        self.base64_number = base64.b64encode(self.number.encode('utf-8'))
        self.number_key = '{0}_number'.format(self.base64_number)
        self.stations_key = '{0}_{1}_stations'.format(self.base64_number, self.stop_type)
        self.stops_key = '{0}_{1}_stops'.format(self.base64_number, self.stop_type)
        self.sid = self.get_sid()

    def get_sid(self):
        # 获取sid信息
        sid = client.get(name=self.number_key)
        if sid:
            return sid
        else:
            res = self.session.post(url=self.sid_url, headers=headers, data={'idnum': self.number}).json()
            sid = res['sid']
            client.set(name=self.number_key, value=sid, ex=SID_TTL)
            return sid

    def get_stations(self):
        # 获取站名数据
        stations = client.hgetall(self.stations_key)
        if stations:
            self.stations = stations
        else:
            res = self.session.get(self.station_url.format(self.sid, self.stop_type), headers=headers).text
            soup = BeautifulSoup(res, 'html.parser')
            for station in soup.find_all(attrs={'class': 'station'}):
                num = station.find_all(attrs={'class': 'num'}, limit=1)[0].text.rstrip('.')
                name = station.find_all(attrs={'class': 'name'}, limit=1)[0].text
                client.hset(self.stations_key, num, name)
                self.stations.update({num: name})
            client.expire(self.stations_key, STATIONS_TTL)
        return self.stations

    def get_stops(self):
        # 获取停靠数据
        stops = client.lrange(self.stops_key, 0, -1)
        if stops:
            self.stops = sorted([json.loads(x) for x in stops], key=lambda x: int(x['stop_id']))
        else:
            for stop_id, station_name in self.stations.iteritems():
                data = {'stoptype': self.stop_type, 'stopid': '{0}.'.format(stop_id), 'sid': self.sid}
                res = self.session.post(self.stop_url, headers=headers, data=data).json()
                res = res if isinstance(res, dict) else res[0]
                info = StopInfo(stop_id=stop_id, station_name=station_name, **res)
                client.lpush(self.stops_key, json.dumps(info.dumps()))
                self.stops.append(info.dumps())
                self.stops = sorted(self.stops, key=lambda x: int(x['stop_id']))
                client.expire(self.stops_key, STOPS_TTL)
        return self.stops
