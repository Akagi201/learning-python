#!/usr/bin/env python

"""Using glob to find files matching a pattern with a filename extension.

"""

import glob

for name in glob.glob('*.py'):
    print name
