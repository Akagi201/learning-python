# -*- coding: utf-8 -*-

# eval
def main():
    dictString = "{'Define1':[[63.3,0.00,0.5,0.3,0.0],[269.3,0.034,1.0,1.0,0.5]," \
                 "[332.2,0.933,0.2,0.99920654296875,1],[935.0,0.990,0.2,0.1,1.0]]," \
                 "'Define2':[[63.3,0.00,0.5,0.2,1.0],[269.3,0.034,1.0,0.3,0.5]," \
                 "[332.2,0.933,0.2, 0.4,0.6],[935.0,0.990,1.0, 0.5,0.0]],}"
    dict = eval(dictString)

    print("keys: ", dict.keys())
    print("Define1 value ", dict['Define1'])

# execfile
#execfile("test_list.py")

main()

# eval(expression[, globals[, locals]])
# 如果忽略后面两个参数，则eval在当前作用域执行。
a = 1
b = eval("a + 1")
print(b)

# 如果指定globals参数
a = 1
g = {'a': 10}
b= eval("a + 1", g)
print(b)

# 如果指定locals参数
a = 10
b = 20
c = 20
g = {'a': 6, 'b': 8}
l = {'b': 9, 'c': 10}
d = eval("a+b+c", g, l)
print(d)

# 如果要严格限制eval执行，可以设置globals为__builtins__,这样 这个表达式只可以访问__builtin__ module。
