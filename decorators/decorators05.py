"""
Example 05
"""
from decorators import debug

@debug
def make_greeting(name, age=None):
    """Using decorator to debug functions"""
    if age is None:
        return f"Howdy {name}"
    return f"Whoa {name}! {age} already, you are growing up!"

print(make_greeting("Dimitri", 36))
