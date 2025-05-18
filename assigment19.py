"""
Create a class Multiplier with an __init__() to set a factor. 
Define a __call__() method that multiplies an input by the factor. 
Test it with callable() and by calling the object like a function.
"""

class Multiplier:
    
    # The __init__ method is called when an instance of the class is created
    def __init__(self,factor):
        self.factor = factor
        
    # The __call__ method allows the instance to be called like a function
    def __call__(self, number):
        return number * self.factor
    
# Test the Multiplier class
multi = Multiplier(5)
print(callable(multi))  # Check if the object is callable
print(multi(10))  # Call the object like a function 