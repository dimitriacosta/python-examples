"""
Example 04
"""
from decorators import timer

@timer
def waste_some_time(num_times):
    """Returning values from the decorator"""
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(999)
