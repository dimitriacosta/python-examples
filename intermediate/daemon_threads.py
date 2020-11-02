"""
Daemon threads example
"""
import threading
import time

PATH = "text.txt"
TEXT = ""

def read_file():
    """Read file in daemon mode"""
    global PATH, TEXT
    while True:
        with open(PATH, "r") as file:
            TEXT = file.read()
        time.sleep(3)

def printloop():
    """Print the content of the file"""
    for _ in range(30):
        print(TEXT)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
