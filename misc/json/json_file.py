#!/usr/bin/env python2

# -*- coding: utf-8 -*-

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# json_str = json.dumps(data)
#
# print(json_str)
#
# data_back = json.loads(json_str)
#
# print(type(data_back))

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data_back = json.load(f)

print(type(data_back))