"""
Threads example
"""
import threading

def hello():
    """Create thread to print a message"""
    for _ in range(50):
        print("Hello!")

t1 = threading.Thread(target=hello)
t1.start()

t1.join()

print("Another text")
