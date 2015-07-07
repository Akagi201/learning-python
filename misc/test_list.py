# -*- coding: utf-8 -*-

# 可以看出这四种方式都可以向列表中添加一个新元素,除了"+"之外，其他三种方式都是在原列表上添加数据，
# "+"则会创建一个新的列表，并且"+"只能连接两个列表，如果连接一个元素跟一个列表会报错

# 添加一个元素到列表中
a = ["a", "b", "c"]
print ("append|添加前id:%s" % id(a)),
a.append("d")
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("extend|添加前id:%s" % id(a)),
a.extend("d")
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("     +|添加前id:%s" % id(a)),
a = a + ["d"]
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("    +=|添加前id:%s" % id(a)),
a += "d"
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

# append方法当添加的元素是列表时会回将整个列表添加进原列表，extend与"+="的效果是一样的，
# 会将列表中的元素添加到原列表，"+"也会将两个列表中的元素复制到一个新创建的列表中，所不同的会创建一个新的列表

# 添加一个列表到列表中
a = ["a", "b", "c"]
print ("append|添加前id:%s" % id(a)),
a.append(["d", "e", "f"])
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("extend|添加前id:%s" % id(a)),
a.extend(["d", "e", "f"])
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("     +|添加前id:%s" % id(a)),
a = a + ["d", "e", "f"]
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)

a = ["a", "b", "c"]
print ("    +=|添加前id:%s" % id(a)),
a += ["d", "e", "f"]
print ("添加后id:%s, %s" % (id(a), a))
print ("-"*62)
