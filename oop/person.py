class Person:

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

    def get_older(years):
        self.age += years

person1 = Person("Dimitri", 37, 172)
print(person1)

person2 = Person("Ale", 34, 148)

del person2

print(Person.amount)
