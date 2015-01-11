#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy
import simplejson as json

attrs = {
  'BC' : 'BirthCountry',
  'G' : 'Gender',
  'CC' : 'CitizenshipCountry',
  'CB' : 'CitizenshipBasis',
  'PC' : 'PassportCountry',
  'CETP' : 'CurrentEmploymentType',
  'CETT' : 'CurrentEmploymentTitle',
  'MSB' : 'MilitaryServiceBranch',
  'MDT' : 'MilitaryDischargeType'
}

count_table = {}
email_table = {}
cluster = {}
content = {}
new_links = []

def organize(cluster, nodes, key):
  global attrs
  global new_links
  global content
  group = 0
  for keyattr in cluster.keys():
    childlist = cluster[keyattr]
    for childid in childlist:
      nodes[childid]['group'] = group
    group += 1
  outputs = {'nodes' : copy.deepcopy(nodes), 'links' : new_links}
  content[attrs[key]] = outputs

def clustering(nodes, key):
  global cluster
  cluster = {}
  for node in nodes:
    attrValue = node[attrs[key]]
    if not cluster.has_key(attrValue):
      cluster[attrValue] = []
    cluster[attrValue].append(int(node['Number']))
  organize(cluster, nodes, key)

jsonobj = json.load(file('Employee Records.json', 'r'))
nodes = jsonobj['nodes']
links = json.load(file('email.json', 'r'))
for node in nodes:
  email_table[node['EmailAddress']] = int(node['Number'])

# Handle the fucking links
for link in links:
  new_link = {}
  if email_table.has_key(link['source']):
    new_link['source'] = email_table[link['source']]
  else:
    continue
  if email_table.has_key(link['target']):
    new_link['target'] = email_table[link['target']]
  else:
    continue
  key = str(new_link['source']) + '_' + str(new_link['target'])
  if count_table.has_key(key):
    count_table[key] += 1
  else:
    count_table[key] = 0
for t in count_table.keys():
  new_link = {}
  new_link['value'] = count_table[t]
  t = t.split('_')
  new_link['source'] = int(t[0])
  new_link['target'] = int(t[1])
  new_links.append(new_link)

# Handle the fucking nodes
for key in attrs:
  clustering(nodes, key)

outputfile = file('content.json', 'w')
outputfile.write(json.dumps(content, indent = 2, sort_keys = True))
outputfile.close()
