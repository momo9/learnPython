#!/usr/bin/python

import json

with open('hello.dat') as fd:
    data = fd.read()

print data

obj = {
    'name': 'momo9',
    'equipments': [
        'mouse',
        'keyboard',
        'screen'
    ]
}

with open('test.json', 'w') as fd:
    json.dump(obj, fd)

with open('test.json') as fd:
    o = json.load(fd)

for k, v in o.items():
    print '%s: %s' % (k, v)
