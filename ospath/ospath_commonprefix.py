#!/usr/bin/env python
# encoding: utf-8

"""Find the prefix string common to a group of paths.
"""

import os.path

paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
print paths
print os.path.commonprefix(paths)
