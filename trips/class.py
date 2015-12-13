class Test(object):
    def test(self):
        pass

a = Test()

b = Test()

print(a.test is b.test) // False

print(id(a.test) == id(b.test)) // True
