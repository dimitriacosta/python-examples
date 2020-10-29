"""
Instance method example
"""
class Dog:
    """Define a dog"""

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        """Return dog's description"""
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        """Return the dog's sound"""
        return f"{self.name} says {sound}"

# Instantiate the dog object
mikey = Dog('Mikey', 6)

print(mikey.description())
print(mikey.speak("Gruff Gruff"))
