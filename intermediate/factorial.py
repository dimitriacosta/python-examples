"""
Calculate the factorial of a number
"""
NUM = 7

FACTORIAL = 1
while NUM > 0:
    FACTORIAL = FACTORIAL * NUM
    NUM -= 1

print(FACTORIAL)

def factorial(value):
    """Generate the factorial value of a number"""
    if value < 1:
        return 1
    value = value * factorial(value - 1)
    return value

print(factorial(7))
