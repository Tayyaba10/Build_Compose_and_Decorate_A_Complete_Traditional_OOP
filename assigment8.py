"""
Create a class Person with a constructor that sets the name.
Inherit a class Teacher from it, add a subject field, and 
use super() to call the base class constructor.
"""

# Define the Person class
class Person():
    def __init__(self, name):
        self.name = name

# Create a class Teacher that inherits from Person        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) # Call the base class constructor
        self.subject = subject

# Create an instance of Teacher and print the name and subject        
t = Teacher("Tayyaba", "Python")
print(f"Name: {t.name} \nSubject: {t.subject}")