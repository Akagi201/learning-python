#!/usr/bin/env python

'''
try:
     Normal execution block
except A:
     Exception A handle
except B:
     Exception B handle
except:
     Other exception handle
else:
     if no exception,get here
finally:
     print("finally")
'''


class AError(Exception):
    """AError---exception"""
    print('AError')


try:
    # raise AError
    asdas('123')
except AError:
    print("Get AError")
except:
    print("exception")
else:
    print("else")
finally:
    print("finally")
print("hello wolrd")
