import os
from _bridge import ffi

lib = ffi.dlopen(os.path.join(os.path.dirname(__file__), "libbridge.so"))


def FormatOneInt(fmt, a):
    return ffi.string(lib.FormatOneInt(fmt, a))