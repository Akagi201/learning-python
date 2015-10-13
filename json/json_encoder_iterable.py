#!/usr/bin/env python
# encoding: utf-8

import json

encoder = json.JSONEncoder()
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]

for part in encoder.iterencode(data):
    print 'PART:', part
