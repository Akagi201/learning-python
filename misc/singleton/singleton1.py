# -*- coding: UTF-8 -*-

# 如果想使得某个类从始至终最多只有一个实例, 使用__new__方法会很简单.
# 方法1, 实现__new__方法
# 并在将一个类的实例绑定到类变量_inst上
# 如果cls._inst为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._inst不为None,直接返回cls._inst

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst=super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

if __name__ == '__main__':
    class A(Singleton):
        def __init__(self, s):
            self.s = s
    a = A('apple')
    b = A('banana')
    print id(a), a.s
    print id(b), b.s
