# coding=utf-8

# redis连接信息
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = ''

# redis缓存时间
# 缓存SID时间 理论上一部车对应一个SID
SID_TTL = 86400
# 缓存车站信息 理论上不会改变
STATIONS_TTL = 86400
# 缓存到站信息 30秒内不刷新
STOPS_TTL = 30
