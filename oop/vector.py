"""
Examples with vectors
"""
class Vector:
    """Define a vector"""

    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    def __add__(self, other):
        return Vector(self.x_value + other.x_value, self.y_value + other.y_value)

    def __sub__(self, other):
        return Vector(self.x_value - other.x_value, self.y_value - other.y_value)

    def __str__(self):
        return f"X: {self.x_value}, Y: {self.y_value}"

v1 = Vector(2, 5)
v2 = Vector(6, 3)

print(f"V1 = {v1}")
print(f"V2 = {v2}")

v3 = v1 + v2

print(f"V1 + V2 = {v3}")
