#!/usr/bin/env python2

# http://tulpar008.github.io/python-withyu-ju.html

class Sample:
    def __enter__(self):
        print("In __enter__()")
        return self

    def __exit__(self, type, value, trace):
        print("In __exit__()")
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()
