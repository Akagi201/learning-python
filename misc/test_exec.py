# -*- coding: utf-8 -*-
# Exec与Eval语句的区别: Exec处理字符串里的代码, 而Eval是处理字符串里面的表达式.
# exec_stmt ::=  "exec" or_expr ["in" expression ["," expression]]
# exec的第一个表达式可以是
# 代码字符串
# 文件对象
# 代码对象
# tuple

# test1 如果忽略后面的可选表达式,exec后面代码将在当前域执行
a = 2
exec "a=1"
print(a)

# test2 如果在表达式之后使用in选项指定一个dic，它将作为global和local变量作用域
a = 10
b = 20
g = {'a': 6, 'b': 8}
exec "global a; print a,b" in g
exec "b; print a,b" in g

# test3 如果in后详指定两个表达式，它们将分别用作global和local变量作用域
a = 10
b = 20
c = 20
g = {'a': 6, 'b': 8}
l = {'b': 9, 'c': 10}
exec "global b; print a, b, c" in g, l

# tuple
#  exec(expr, globals) #它等效于  exec expr in globals
# exec(expr, globals, locals) #它等效于  exec expr in globals,locals


