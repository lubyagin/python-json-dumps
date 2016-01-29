#!/usr/bin/python
# -*- coding: utf-8 -*-
# Пример кодирования объекта типа datetime в JSON с помощью внешней функции

import json
import datetime
import decimal

t = datetime.datetime.now()
print type(t)

def serialize(o):
  if isinstance(o,datetime.datetime):
    s = o.isoformat()
    return s
  else:
    return ""

s = json.dumps({"time":t},default=serialize)
print s

o = json.loads(s)
print o

# Ручная замена строк
import re
r_date = re.compile("(\d{4}-\d{2}-\d{2}).*")
n = "time"
res = r_date.findall(o[n])
if res <> []: o[n] = res[0]
print o

p = lambda:None # http://stackoverflow.com/questions/15476983/deserialize-a-json-string-to-an-object-in-python
p.__dict__ = json.loads(s)
print p.time

# Error in print json.dumps([t])
# TypeError: datetime.datetime(2016, 1, .., .., .., .., ....) is not JSON serializable

# <type 'datetime.datetime'>
# ["2016-01-19T08:30:09.242000"]
# [u'2016-01-19T08:30:09.242000']

# Пример кодирования объекта типа Numeric в JSON с помощью внешней функции

print "None :", json.dumps([None]) # [null]
print "True :", json.dumps([True]) # [true]
print "False:", json.dumps([False]) # [false]
print "1.23 :", json.dumps([1.23]) # [1.23]
# print "1+2j :", json.dumps([1+2j]) # TypeError: (1+2j) is not JSON serializable
print "100L :", json.dumps([100L]) # [100]
print "u''  :", json.dumps([u'привет']) # ["\u043f\u0440\u0438\u0432\u0435\u0442"]
print "{..} :", json.dumps([{"1":"2"}]) # [{"1": "2"}]
print "(..) :", json.dumps([("1","2")]) # [["1", "2"]]

class MyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
      return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
      return float(obj)
    else:
      return json.JSONEncoder.default(self, obj)

t = datetime.datetime.now()
print json.dumps([t],cls=MyEncoder)
t = datetime.date.today()
print json.dumps([t],cls=MyEncoder)
n = decimal.Decimal('123.45')
print json.dumps({'n': n},cls=MyEncoder)
