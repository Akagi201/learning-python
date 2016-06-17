#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis, time, random

rc = redis.StrictRedis(host='localhost', port=6379, db=0)


def wait(wait_for):
    ps = rc.pubsub()
    ps.subscribe(wait_for)
    ps.get_message()
    wait_msg = None
    while True:
        msg = ps.get_message()
        if msg and msg['type'] == 'message':
            wait_msg = msg
        break
    time.sleep(0.001)
    ps.close()
    return wait_msg


def signal_broadcast(wait_in, data):
    wait_count = rc.publish(wait_in, data)
    return wait_count


single_cast_script = """
    local channels = redis.call('pubsub', 'channels', ARGV[1]..'*');
    if #channels == 0 then
        return 0;
    end;
    local index = math.mod(math.floor(tonumber(ARGV[2])), #channels) + 1;
    return redis.call('publish', channels[index], ARGV[3]);
"""


def wait_single(channel, myid):
    return wait(channel + myid)


def signal_single(channel, data):
    rand_num = int(random.random() * 65535)
    return rc.eval(single_cast_script, 0, channel, str(rand_num), str(data))
