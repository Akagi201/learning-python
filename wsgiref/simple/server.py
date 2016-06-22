#!/usr/bin/env python
# -*- coding:utf-8 -*-

# server.py
# 从 wsgiref 模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的 application 函数
from hello import application

# 创建一个服务器, IP 地址为空, 端口是 8000, 处理函数是 application
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听 HTTP 请求
httpd.serve_forever()
