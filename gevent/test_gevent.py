#!/usr/bin/env python

import gevent
from gevent import socket

urls = ['www.baidu.com', 'www.163.com', 'www.qq.com']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)

print([job.value for job in jobs])
