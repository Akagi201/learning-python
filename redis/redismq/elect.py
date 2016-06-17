#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

rc = redis.StrictRedis(host='localhost', port=6379, db=0)
local_selector = 0


def master():
    global local_selector
    master_selector = rc.incr('master_selector')
    if master_selector == 1:
        # initial / restarted
        local_selector = master_selector
    else:
        if local_selector > 0:
            # I'm the master before
            if local_selector > master_selector:
                # lost, maybe the db is fail-overed.
                local_selector = 0
            else:
                # continue to be the master
                local_selector = master_selector
    if local_selector > 0:
        # I'm the current master
        rc.expire('master_selector', 20)
    return local_selector > 0
