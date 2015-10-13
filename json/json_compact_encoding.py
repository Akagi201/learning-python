#!/usr/bin/env python
# encoding: utf-8

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print 'DATA:', repr(data)
print 'repr(data)             :', len(repr(data))
print 'dumps(data)            :', len(json.dumps(data))
print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=2))
print 'dumps(data, separators):', len(json.dumps(data, separators=(',', ':')))
print 'dumps(data, separators):', json.dumps(data, separators=(',', ':'))
