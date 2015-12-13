* 可变默认参数，闭包陷阱: <http://docs.python-guide.org/en/latest/writing/gotchas/>
* 浮点数相关问题，好多语言都这样，如果不这样实现性能会大打折扣。 list 和 class 的引用可以算俩坑。列表楼上易经说了，类循环引用会造成内存泄漏。看看这个就知道了 <https://docs.python.org/3/library/weakref.html> 不过其他语言里也有呀。
* 默认参数不是每次都初始化
* lambda 只能一行且不能出现 statement
* python2 弱类型: 2 >"WTF" => False
* py2 多返回值: a, b = 1,2,3 会报错
* StandardError 经常 catch 不到东西，大多数都得上 Exception
* 没 switch, 大段 if 真的很丑
* 推荐 format 方法来格式化，但是 log 中却还是旧的字符串格式化
* 还有个比较坑的地方是 os.path.join 和 str.join 用法不一样， str.join 接受 iterable 做参数， os.path.join 可以接受可变参数。。。。。用错也没提示，真坑。
* urljoin 和预期不同，不能接受多个参数，必须一个个嵌套，而且第一个参数如果格式错误也会返回很奇怪的结果
* 列表解析里的变量作用域外泄
* 
