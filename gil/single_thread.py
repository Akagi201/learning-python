#!/usr/bin/env python

from threading import Thread
import time

def my_counter():
    i = 0
    for _ in range(100000000):
        i = i + 1
    return True

def main():
    start_time = time.time()
    for _ in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time - start_time))

if __name__ == '__main__':
    main()