#!/usr/bin/env python
# encoding: utf-8

"""Simple MD5 generation.
"""

__version__ = "$Id$"

import hashlib
from hashlib_data import lorem

h = hashlib.md5()
h.update(lorem)
print h.hexdigest()
