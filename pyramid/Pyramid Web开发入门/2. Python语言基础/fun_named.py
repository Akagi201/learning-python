def test(a, b=50, c=60):
    print 'a=%s, b=%s, c=%s' % (a, b, c)


test(1)
test(1, 5)
test(1, c=10)
