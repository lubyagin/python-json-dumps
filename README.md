Convert datetime, Numeric etc. to JSON-string

http://pythonworld.ru/moduli/modul-json.html

Класс json.JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

```
@C:\Python27\python.exe datetime-json.py
print type(t) # datetime.datetime.now()
<type 'datetime.datetime'>
> print json.dumps([t],default=serialize)
["2016-01-19T08:30:09.242000"]
> print json.loads(s)
[u'2016-01-19T08:30:09.242000']
```

Другие простейшие типы:
```
print "None :", json.dumps([None]) # [null]
print "True :", json.dumps([True]) # [true]
print "False:", json.dumps([False]) # [false]
print "1.23 :", json.dumps([1.23]) # [1.23]
# print "1+2j :", json.dumps([1+2j]) # TypeError: (1+2j) is not JSON serializable
print "100L :", json.dumps([100L]) # [100]
print "u''  :", json.dumps([u'привет']) # ["\u043f\u0440\u0438\u0432\u0435\u0442"]
print "{..} :", json.dumps([{"1":"2"}]) # [{"1": "2"}]
print "(..) :", json.dumps([("1","2")]) # [["1", "2"]]
```

```
<type 'datetime.datetime'>
{"time": "2016-01-29T08:36:31.077000"}
{u'time': u'2016-01-29T08:36:31.077000'}
{u'time': u'2016-01-29'}
2016-01-29T08:36:31.077000
None : [null]
True : [true]
False: [false]
1.23 : [1.23]
100L : [100]
u''  : ["\u043f\u0440\u0438\u0432\u0435\u0442"]
{..} : [{"1": "2"}]
(..) : [["1", "2"]]
["2016-01-29T08:36:31.077000"]
["2016-01-29"]
{"n": 123.45}
```
