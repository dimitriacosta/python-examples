"""
First class example
"""
class Dog:
    """Define a dog"""

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        """Return the dog's age"""
        return self.age
    def get_name(self):
        """Return the dog's name"""
        return self.name

jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)

# Determine the oldest dog
def get_biggest_number(*args):
    """Get the oldest dog"""
    return max(args)

print(f"The oldest dog is {get_biggest_number(jake.age, doug.age, william.age)} years old.")
