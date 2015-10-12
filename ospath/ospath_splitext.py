#!/usr/bin/env python
# encoding: utf-8

"""Separate a filename into the base and extension.
"""

import os.path

for path in ['filename.txt', 'filename', '/path/to/filename.txt', '/', '']:
    print '"%s" :' % path, os.path.splitext(path)
