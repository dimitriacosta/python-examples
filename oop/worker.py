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

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        return f"{text}, Salary: {self.salary}"

    def calc_yearly_salary(self):
        return f"Yearly salary is: ${self.salary * 12:.2f}"

worker1 = Worker("Dimitri", 37, 172, 3000)
print(worker1)
print(worker1.calc_yearly_salary())
