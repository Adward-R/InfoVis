#!/usr/bin/python
# -*- coding: utf-8 -*-
import simplejson as json

csvfile = file('email headers.csv', 'r')
line = csvfile.readline().strip()
headers = line.split(',')
links = []

line = csvfile.readline()
while len(line) != 0:
  headers = line.split('"')
  if len(headers) > 1:
    From = headers[0].split(',')[0].strip()
    Tos = headers[1].split(',')
    for To in Tos:
      item = {
        "source": From,
        "target": To.strip(),
        "time": 1
      }
      links.append(item)
  else:
    headers = headers[0].split(',')
    From = headers[0].strip()
    To = headers[1].strip()
    item = {
      "source": From,
      "target": To,
      "time": 1
    }
    links.append(item)
  line = csvfile.readline()
output = file('email.json', 'w')
output.write(json.dumps(links, indent = 2, sort_keys = True))
