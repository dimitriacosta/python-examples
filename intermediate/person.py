"""
Person class example
"""
class Person:
    """Define a person"""

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

    def get_older(self, years):
        """Increase person's age"""
        self.age += years

person1 = Person("Dimitri", 37, 172)
print(person1)
print(f"Increase {person1.name}'s age by 1")
person1.get_older(1)
print(person1)

print("Adding a new person")
person2 = Person("Ale", 34, 148)
print(person2)
print(f"Number of class Person instances {Person.amount}")

print(f"Deleting {person2.name}")
del person2

print(f"Number of class Person instances {Person.amount}")
