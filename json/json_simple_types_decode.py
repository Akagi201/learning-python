#!/usr/bin/env python
# encoding: utf-8

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
data_string = json.dumps(data)
print 'ENCODED:', data_string

# In particular, strings are converted to unicode and tuples become lists.

decoded = json.loads(data_string)
print 'DECODED:', decoded

print 'ORIGINAL:', type(data[0]['b'])
print 'DECODED :', type(decoded[0]['b'])
