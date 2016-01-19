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

s = json.dumps([t],default=serialize)
print s

o = json.loads(s)
print o

# Error in print json.dumps([t])
# TypeError: datetime.datetime(2016, 1, .., .., .., .., ....) is not JSON serializable
