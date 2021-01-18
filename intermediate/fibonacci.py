"""
Generate fibonacci number based on a position
"""
def fibonacci1(num):
    """Non recursive function."""
    first_value, second_value = 0, 1
    for _ in range(num):
        first_value, second_value = second_value, first_value + second_value
    return first_value

print(fibonacci1(6))


def fibonacci2(value):
    """Recursive function"""
    if value <= 1:
        return value
    return fibonacci2(value - 1) + fibonacci2(value - 2)

print(fibonacci2(6))
