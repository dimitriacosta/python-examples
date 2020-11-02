"""
Locking threads example
"""
import threading
import time

X = 8192

LOCK = threading.Lock()

def double():
    """Double the number"""
    global X, LOCK
    LOCK.acquire()
    while X < 16384:
        X *= 2
        print(X)
        time.sleep(1)
    print("Reached the maximum")
    LOCK.release()

def halve():
    """Halve the number"""
    global X, LOCK
    LOCK.acquire()
    while X > 1:
        X /= 2
        print(X)
        time.sleep(1)
    print("Reached the minimum")
    LOCK.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
