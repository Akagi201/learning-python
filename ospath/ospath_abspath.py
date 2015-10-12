#!/usr/bin/env python
# encoding: utf-8

"""Compute an absolute path from a relative path.
"""

import os.path

for path in ['.', '..', './one/two/three', '../one/two/three']:
    print '"%s" : "%s"' % (path, os.path.abspath(path))
