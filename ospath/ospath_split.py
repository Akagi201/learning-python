#!/usr/bin/env python
# encoding: utf-8

"""Separate a path into its directory and base components.
"""

import os.path

for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print '"%s" : "%s"' % (path, os.path.split(path))
