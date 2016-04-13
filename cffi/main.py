from _simple_example import ffi

lib = ffi.dlopen(None)      # Unix: open the standard C library
#import ctypes.util         # or, try this on Windows:
#lib = ffi.dlopen(ctypes.util.find_library("c"))

lib.printf(b"hi there, number %d\n", ffi.cast("int", 2))
