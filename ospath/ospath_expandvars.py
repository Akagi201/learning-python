#!/usr/bin/env python
# encoding: utf-8

"""Expand shell variables in filenames.
"""

import os.path
import os

os.environ['MYVAR'] = 'VALUE'

print os.path.expandvars('/path/to/$MYVAR')
