"""
Use the abc module to create an abstract class Shape with 
an abstract method area(). Inherit a class Rectangle that implements area().
"""

# Import the abc module to create an abstract class
from abc import ABC, abstractmethod

class Shape(ABC):
    # Define the abstract method area
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    
    # Constructor to initialize the rectangle's dimensions
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    # Implement the area method
    def area(self):
        return self.height * self.width

rect = Rectangle(3,6)
print(f"Area of the rectangle: {rect.area()}")