
from threading import Timer

def delayed(seconds):
    def decorator(f):
        def wrapper(*args, **kargs):
            t = Timer(seconds, f, args, kargs)
            t.start()
        return wrapper
    return decorator

@delayed(3)
def timer_print():
    print "timer_print"

for i in range(3):
    timer_print()