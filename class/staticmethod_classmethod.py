
#!/usr/bin/env python
# http://blog.csdn.net/handsomekang/article/details/9615239

class A(object):
    bar = 1
    def foo(self):
        print 'foo'

    @staticmethod
    def static_foo():
        print 'static_foo'
        print A.bar

    @classmethod
    def class_foo(cls):
        print 'class_foo'
        print cls.bar
        cls().foo()

A.static_foo()
A.class_foo()
A().foo()
