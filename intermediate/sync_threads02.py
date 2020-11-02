"""
Thread semaphore example
"""
import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(num):
    """Define class to use the semaphore"""
    print(f"{num} is trying to access!")
    semaphore.acquire()
    print(f"{num} granted access!")
    time.sleep(5)
    print(f"{num} is now releasing!")
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)
