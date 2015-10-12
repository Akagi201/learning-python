#!/usr/bin/env python
# encoding: utf-8

"""Determine the base filename from a path.
"""

import os.path

for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print '"%s" : "%s"' % (path, os.path.basename(path))
