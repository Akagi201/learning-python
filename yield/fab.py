
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

# fab(5)

def fab1(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

# for n in fab1(5):
#     print n

# for i in range(1000):
#     print i
#
# for i in xrange(1000):
#     print i

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

for n in Fab(5):
    print n

def fab2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# for n in fab(5):
#     print n

f = fab2(5)
f.next()

from inspect import isgeneratorfunction

print(isgeneratorfunction(fab2))

import types

print(isinstance(fab2, types.GeneratorType))
print(isinstance(fab2(5), types.GeneratorType))

from collections import Iterable
print(isinstance(fab2, Iterable))
print(isinstance(fab2(5), Iterable))

def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return