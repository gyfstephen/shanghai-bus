# coding=utf-8

from flask import Flask, jsonify
from bus import Bus

app = Flask(__name__)


class Response(object):
    def __init__(self, error=0, msg='', data=None):
        self.error = error
        self.msg = msg
        self.data = data

    def dumps(self):
        return {'error': self.error, 'msg': self.msg, 'data': self.data}


@app.route('/api/v1/stations/<string:stop_type>/<int:number>/')
def get_stations(stop_type, number):
    if stop_type not in ['up', 'down']:
        return jsonify(Response(error=1, msg='stop type error').dumps())
    bus = Bus(number=number, stop_type={'up': 0, 'down': 1}[stop_type])
    stations = bus.get_stations()
    return jsonify(Response(error=0, msg='', data=stations).dumps())


@app.route('/api/v1/stops/<string:stop_type>/<int:number>/')
def get_stops(stop_type, number):
    if stop_type not in ['up', 'down']:
        return jsonify(Response(error=1, msg='stop type error').dumps())
    bus = Bus(number=number, stop_type={'up': 0, 'down': 1}[stop_type])
    bus.get_stations()
    stops = bus.get_stops()
    return jsonify(Response(error=0, msg='', data=stops).dumps())


if __name__ == '__main__':
    app.run()
