# 上海公交信息API查询
数据来源：上海发布

API接口：

- 查询车辆站台信息

  ```
  /api/v1/stations/<string:stop_type>/<int:number>/
  ```

- 查询车辆到站信息

  ```
  /api/v1/stops/<string:stop_type>/<int:number>/
  ```

示例：

- 查询公交100上行站台信息 /api/v1/stations/up/110/

```json
{
    "data": {
        "1": "吉浦路仁德路", 
        "2": "武川路武东路", 
        "3": "武川路政立路", 
        "4": "政立路国权北路", 
        "5": "政立路逸仙路", 
        "6": "逸仙路场中路", 
        "7": "江湾(逸仙路)", 
        "8": "逸仙路纪念路", 
        "9": "大柏树(曲阳路)", 
        "10": "曲阳路中山北二路", 
        "11": "大连西路曲阳路", 
        "12": "欧阳路大连西路", 
        "13": "欧阳路祥德路", 
        "14": "欧阳路四达路", 
        "15": "欧阳路吉祥路", 
        "16": "四平路溧阳路", 
        "17": "吴淞路海宁路", 
        "18": "吴淞路天潼路"
    }, 
    "error": 0, 
    "msg": ""
}
```

- 查询公交100上行到站信息 /api/v1/stops/up/110/

```json
{
    "data": [
        {
            "distance": 0, 
            "error": 0, 
            "plate": "沪A-00737D", 
            "station_name": "吉浦路仁德路", 
            "stop_dis": 1, 
            "stop_id": 1, 
            "time": 929
        }, 
        {
            "distance": 1296, 
            "error": 0, 
            "plate": "沪A-00737D", 
            "station_name": "武川路武东路", 
            "stop_dis": 1, 
            "stop_id": 2, 
            "time": 1048
        }, 
        {
            "distance": 1548, 
            "error": 0, 
            "plate": "沪A-00737D", 
            "station_name": "武川路政立路", 
            "stop_dis": 2, 
            "stop_id": 3, 
            "time": 1110
        }, 
        {
            "distance": 2203, 
            "error": 0, 
            "plate": "沪A-00737D", 
            "station_name": "政立路国权北路", 
            "stop_dis": 3, 
            "stop_id": 4, 
            "time": 1289
        }, 
        {
            "distance": 576, 
            "error": 0, 
            "plate": "沪A-01825D", 
            "station_name": "政立路逸仙路", 
            "stop_dis": 1, 
            "stop_id": 5, 
            "time": 88
        }, 
        {
            "distance": 1175, 
            "error": 0, 
            "plate": "沪A-01825D", 
            "station_name": "逸仙路场中路", 
            "stop_dis": 2, 
            "stop_id": 6, 
            "time": 208
        }, 
        {
            "distance": 1590, 
            "error": 0, 
            "plate": "沪A-01825D", 
            "station_name": "江湾(逸仙路)", 
            "stop_dis": 3, 
            "stop_id": 7, 
            "time": 269
        }, 
        {
            "distance": 1882, 
            "error": 0, 
            "plate": "沪A-01825D", 
            "station_name": "逸仙路纪念路", 
            "stop_dis": 4, 
            "stop_id": 8, 
            "time": 388
        }, 
        {
            "distance": 3142, 
            "error": 0, 
            "plate": "沪A-01825D", 
            "station_name": "大柏树(曲阳路)", 
            "stop_dis": 5, 
            "stop_id": 9, 
            "time": 628
        }, 
        {
            "distance": 293, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "曲阳路中山北二路", 
            "stop_dis": 1, 
            "stop_id": 10, 
            "time": 31
        }, 
        {
            "distance": 1642, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "大连西路曲阳路", 
            "stop_dis": 2, 
            "stop_id": 11, 
            "time": 331
        }, 
        {
            "distance": 2170, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "欧阳路大连西路", 
            "stop_dis": 3, 
            "stop_id": 12, 
            "time": 449
        }, 
        {
            "distance": 2579, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "欧阳路祥德路", 
            "stop_dis": 4, 
            "stop_id": 13, 
            "time": 569
        }, 
        {
            "distance": 2867, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "欧阳路四达路", 
            "stop_dis": 5, 
            "stop_id": 14, 
            "time": 630
        }, 
        {
            "distance": 3196, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "欧阳路吉祥路", 
            "stop_dis": 6, 
            "stop_id": 15, 
            "time": 689
        }, 
        {
            "distance": 4019, 
            "error": 0, 
            "plate": "沪A-07566D", 
            "station_name": "四平路溧阳路", 
            "stop_dis": 7, 
            "stop_id": 16, 
            "time": 870
        }, 
        {
            "distance": 728, 
            "error": 0, 
            "plate": "沪A-05870D", 
            "station_name": "吴淞路海宁路", 
            "stop_dis": 1, 
            "stop_id": 17, 
            "time": 90
        }, 
        {
            "distance": 1329, 
            "error": 0, 
            "plate": "沪A-05870D", 
            "station_name": "吴淞路天潼路", 
            "stop_dis": 2, 
            "stop_id": 18, 
            "time": 330
        }
    ], 
    "error": 0, 
    "msg": ""
}
```

TODO:

- [ ] 缓存时间优化
- [ ] 支持查询特定站到站时间
- [ ] 支持查询同一站的多条线路
