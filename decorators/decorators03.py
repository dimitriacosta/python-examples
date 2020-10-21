"""
Example 03
"""
from decorators import do_twice

@do_twice
def return_greeting(name):
    """Using decorator from an external file"""
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
print(hi_adam)
