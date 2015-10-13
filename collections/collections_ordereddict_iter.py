#!/usr/bin/env python
# encoding: utf-8

"""Iterating over an OrderedDict
"""

import collections

print 'Regular dictionary:'
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

print type(d)
for k, v in d.items():
    print k, v

print '\nOrderedDict:'
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['e'] = 'E'
d['d'] = 'D'

print type(d)
for k, v in d.items():
    print k, v
