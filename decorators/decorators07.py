"""
Example 07
"""
from decorators import slow_down

@slow_down
def countdown(from_number):
    """Create down code"""
    if from_number < 1:
        print("Liftoff")
    else:
        print(from_number)
        countdown(from_number - 1)


countdown(3)
