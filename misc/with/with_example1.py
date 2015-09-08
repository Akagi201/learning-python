#!/usr/bin/env python2

# http://tulpar008.github.io/python-withyu-ju.html

class Sample(object):
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

def get_sample():
    return Sample()

if __name__ == "__main__":
    with get_sample() as sample:
        print("sample: %s" % sample)
