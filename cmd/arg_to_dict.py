#!/usr/bin/env python

import sys

def arg_to_dict():
    """
    python program.py key1:val1 key2:val2 key3:val3
    dict = {'key3': 'val3', 'key2': 'val2', 'key1': 'val1'}
    :return:
    """
    dict = {}
    for arg in sys.argv[1:]:
        key, val = arg.split(':')[0], arg.split(':')[1]
        dict[key] = val
    return dict

if __name__ == "__main__":
    arg_dict = arg_to_dict()
    print(arg_dict)
