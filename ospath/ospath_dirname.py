#!/usr/bin/env python
# encoding: utf-8

"""Find the directory portion of a filename.
"""

import os.path

for path in ['/one/two/three',
             '/one/two/three/',
             '/',
             '.',
             '']:
    print '"%s" : "%s"' % (path, os.path.dirname(path))
