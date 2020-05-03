class Dog:

    species = 'mammal'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)

# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(jake.age, doug.age, william.age)))