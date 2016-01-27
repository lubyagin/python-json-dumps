#!/usr/bin/python
# -*- coding: utf-8 -*-
# Пример кодирования объекта типа datetime в JSON
# с помощью внешней функции

import datetime
t = datetime.datetime.now()
print type(t)

import json

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
