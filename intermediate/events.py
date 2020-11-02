"""
Events example
"""
import threading

event = threading.Event()

def myfunction():
    """This function will wait for event to get triggered"""
    print("Waiting for event to trigger...")
    event.wait()
    print("Performing action xyz now...")

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event? (y/n) ")
if x == "y":
    event.set()
