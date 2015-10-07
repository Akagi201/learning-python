#!/usr/bin/env python

"""Example expansion of question mark wild card.

"""

import glob

for name in glob.glob('dir/file?.txt'):
    print name
