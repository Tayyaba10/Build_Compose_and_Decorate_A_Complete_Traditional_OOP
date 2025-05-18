"""
Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
"""

# The code defines a class named Employee with three attributes: name, _salary, and __ssn.
class Employee():  
     
    def __init__(self,name,salary,ssn):
        self.name = name # public variable
        self._salary = salary # protected variable
        self.__ssn = ssn # private variable
        
print("----Employee object created----")
 
# Create an instance of the Employee class       
E1 = Employee("Hira", 20000, "123-45-6789")

# Accessing the variables
print(f"Name: {E1.name}") # Accessing public variable
print(f"Salary: {E1._salary}") # Accessing protected variable
print(f"SSN: {E1.__ssn}") # Attempting to access private variable will raise an AttributeError
print(E1._Employee__ssn) # Accessing private variable