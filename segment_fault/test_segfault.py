#!/usr/bin/env python

# http://knktc.com/2014/05/17/python-segmentation-fault/

import ctypes
lib = ctypes.cdll.LoadLibrary('segfault.so')
print("before fault")
lib.fault()
print("after fault")
