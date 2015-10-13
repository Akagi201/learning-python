#!/usr/bin/env python
# encoding: utf-8

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
a = repr(data)
b = str(data)
print 'type a:', type(a)
print 'type b:', type(b)
print 'DATA:', repr(data)

data_string = json.dumps(data)
print 'JSON:', data_string
