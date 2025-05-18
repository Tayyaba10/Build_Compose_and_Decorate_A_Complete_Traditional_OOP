"""
Create a custom exception InvalidAgeError. Write a function 
check_age(age) that raises this exception if age < 18. Handle it with try...except.
"""

class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    """Check if the provided age is valid (18 or older)."""
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    return print("Age is valid.")
     
try:
    age = int(input("Enter your age:"))
    check_age(age)
except InvalidAgeError as e:
    print(e)
    







