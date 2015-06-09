#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uuid

# 从硬件地址和时间生成
print("uuid1: %r" % uuid.uuid1())

# 从md5算法生成
print("uuid3: %r" % uuid.uuid3(uuid.NAMESPACE_DNS, 'testme'))

# 随机生成
print("uuid4: %r" % uuid.uuid4())

# 从SHA-1算法生成
print("uuid5: %r" % uuid.uuid5(uuid.NAMESPACE_DNS, 'testme'))
