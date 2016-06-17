#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

rc = redis.StrictRedis(host='localhost', port=6379, db=0)


def fifo_push(q, data):
    rc.lpush(q, data)


def fifo_pop(q):
    return rc.rpop(q)


def filo_push(q, data):
    rc.lpush(q, data)


def filo_pop(q):
    return rc.lpop(q)


def safe_fifo_push(q, data):
    rc.lpush(q, data)


def safe_fifo_pop(q, cache):
    msg = rc.rpoplpush(q, cache)
    # check and do something on msg
    rc.lrem(cache, 1)  # remove the msg in cache list.
    return msg
