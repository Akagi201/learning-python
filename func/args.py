# coding: utf-8

# 函数接收元组和列表.
# 参数前面为*, 代表这个位置的参数不知道有多少个参数, 如果有, 则将其存储为元组.

def x(a, b, *c):
    print "第一个参数: " + str(a)
    print "第二个参数: " + str(b)
    print "参数c: " + str(c)
    print "第三个参数为: " + str(c[0])

# 参数前面为**, 代表这个位置的参数不知道有多少个参数, 如果有, 则将其存储为字典
def y(*c, **k):
    print c
    print k

if __name__ == "__main__":
    x(1,2,3,4)
    y(1,2,a="b",c="d")