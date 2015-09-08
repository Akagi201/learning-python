
import time
import threading

def hello(s):
    print(s)

if __name__ == "__main__":
    key = "Akagi201"
    for i in range(3):
        t = threading.Timer(3.0, hello, [key])
        t.start()
    print("Done")
