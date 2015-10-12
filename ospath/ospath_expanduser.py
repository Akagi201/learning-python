#!/usr/bin/env python
# encoding: utf-8

"""Expand tilde in filenames.
"""

import os.path

for user in ['', 'dhellmann', 'postgres']:
    lookup = '~' + user
    print lookup, ':', os.path.expanduser(lookup)
