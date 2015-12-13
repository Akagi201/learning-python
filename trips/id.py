a = [1, 2]
print(id(a))
b = a
print(id(b))
c = a[:]
print(id(c))
d = list(a)
print(id(d))

import copy
e = copy.copy(a)
print(id(e))
