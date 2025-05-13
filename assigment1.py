"""
Create a class Student with attributes name and marks. Use the self keyword to 
initialize these values via a constructor. Add a method display() that prints 
student details.
"""

# Defining the Student class
class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # Method to display student details  
    def display(self):
        # Printing the name and marks of the student
        print(f"Name: {self.name} \nMarks: {self.marks}")

# Creating an instance of the Student class and displaying its details     
s1 = Student("Tayyaba", 80)
s1.display()
