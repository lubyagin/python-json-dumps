# python-JSONEncoder-examples
date, Numeric etc. convert to json-string

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
