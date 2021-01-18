"""
Database programing example
"""
import sqlite3

class Person:
    """Person test class"""

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        """Read users from the DB"""
        self.cursor.execute(f"""
        SELECT * FROM persons WHERE id = {id_number}
        """)

        persons = self.cursor.fetchone()

        self.id_number = id_number
        self.first = persons[1]
        self.last = persons[2]
        self.age = persons[3]

    def insert_person(self):
        """Insert users into the DB"""
        self.cursor.execute(f"""
        INSERT INTO persons  VALUES
        ({self.id_number}, '{self.first}', '{self.last}', {self.age})
        """)

        self.connection.commit()
        self.connection.close()

p1 = Person(7, 'Alex', 'Robbins', 30)
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)

connection.close()
