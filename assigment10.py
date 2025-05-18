"""
Create a class Dog with instance variables name and breed.
Add an instance method bark() that prints a message including the dog's name.
"""

# This is a simple class definition for a Dog
class Dog():
    # This is the constructor method that initializes the instance variables
    def __init__(self,name, bread):
        self.name = name
        self.bread = bread
    
    # This is an instance method that prints a message including the dog's name    
    def bark(self):
        print(f"{self.name} says wolf")

# This is an example of how to create an instance of the Dog class and call the bark method       
dog = Dog("Tommy"," Golden Retriever")
dog.bark()
        