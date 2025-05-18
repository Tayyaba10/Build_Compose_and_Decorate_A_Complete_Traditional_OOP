"""
Create a class Department and a class Employee. Use aggregation 
by having a Department object store a reference to an Employee 
object that exists independently of it.
"""

class Employee:
    def __init__(self,name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
class Department():
    def __init__(self,employee):
        self.employee = employee
        
emp = Employee("Ali", 30, 50000)
dept = Department(emp)
print(f"Employee Name: {dept.employee.name} \nEmployee Age: {dept.employee.age} \nEmployee Salary: {dept.employee.salary}")
        

        