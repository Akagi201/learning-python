# file "simple_example_build.py"

# Note: this particular example fails before version 1.0.2
# because it combines variadic function and ABI level.

from cffi import FFI

ffi = FFI()
ffi.set_source("_simple_example", None)
ffi.cdef("""
    int printf(const char *format, ...);
""")

if __name__ == "__main__":
    ffi.compile()
