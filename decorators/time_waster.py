"""
Example of decorators in classes
"""
from decorators import debug, timer

class TimeWaster:
    """Example of a time waster class"""
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        """Returns the sqares of numbers"""
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_time(999)