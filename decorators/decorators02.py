"""
Example 02
"""
def my_decorator(func):
    """Define our decorator"""
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    """Use the new syntax to decorate a function"""
    print("Whee!")

say_whee()
