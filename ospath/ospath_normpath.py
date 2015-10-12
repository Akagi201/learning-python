#!/usr/bin/env python
# encoding: utf-8

"""Compute a "normalized" path.
"""

import os.path

for path in ['one//two//three',
             'one/./two/./three',
             'one/../one/two/three',
             ]:
    print path, ':', os.path.normpath(path)
