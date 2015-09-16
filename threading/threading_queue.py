#!/usr/bin/env python

import Queue
import threading
import urllib2
import time
from BeautifulSoup import BeautifulSoup

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com", "http://ibm.com", "http://apple.com"]

queue = Queue.Queue()
out_queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    """
    Threaded Url Grab
    """
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            # grabs host from queue
            host = self.queue.get()

            # grabs urls of hosts and then grabs chunk of webpage
            url = urllib2.urlopen(host)
            chunk = url.read()

            # place chunk into out queue
            self.out_queue.put(chunk)

            # signals to queue job is done
            self.queue.task_done()

class DatamineThread(threading.Thread):
    """
    Thread Url Grab
    """
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            # grabs hosts from queue
            chunk = self.out_queue.get()

            # parse the chunk
            soup = BeautifulSoup(chunk)
            print(soup.findAll(['title']))

            # signals to queue job is done
            self.out_queue.task_done()

def main():
    # spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadUrl(queue, out_queue)
        t.setDaemon(True)
        t.start()

    # populate queue with data
    for host in hosts:
        queue.put(host)

    for i in range(5):
        dt = DatamineThread(out_queue)
        dt.setDaemon(True)
        dt.start()

    # wait on the queue until everything has been processed
    queue.join()
    out_queue.join()

if __name__ == "__main__":
    start = time.time()
    main()
    print("Elapsed Time: %s" % (time.time() - start))
