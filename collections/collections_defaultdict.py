#!/usr/bin/env python
# encoding: utf-8

"""Initializing a defaultdict.
"""

import collections


def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print 'd:', d
print 'foo =>', d['foo']
print 'bar =>', d['bar']
print 'empty =>', d.get('empty')
