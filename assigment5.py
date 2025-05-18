"""
Create a class MathUtils with a static method add(a, b) 
that returns the sum. No class or instance variables should be used.
"""

# Define the MathUtils class
class MathUtils():
    
    @staticmethod
    def add(a,b):
        """
        This method takes two numbers and returns their sum.
        """
        return a + b
    
# Test the MathUtils class
print(MathUtils.add(5, 3))  # Output: 8
print(MathUtils.add(-1, 1))  # Output: 0