"""
Create a class decorator add_greeting that modifies a class 
to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
"""

# This is a class decorator that adds a greet method to the class.
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    
    return cls
# This is a class that represents a person.
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        
p = Person("Ali")
print(f"{p.greet()} {p.name}")  # Output: Hello from Decorator!