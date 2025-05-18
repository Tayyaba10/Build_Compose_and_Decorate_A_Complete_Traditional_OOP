"""
Create a class Counter that keeps track of how many objects have been created.
Use a class variable and a class method with cls to manage and display the cou
"""

# Defining the Counter class
class Counter():
    # Class variable to keep track of the count
    count = 0 
    
    # Class method to get the current count
    def __init__(self):
        Counter.count += 1
        
    # Class method to display the count
    @classmethod
    def show_count(cls):
        # Printing the current count of objects created
        print(f"Number of objects created: {cls.count}")

# Creating instances of the Counter class      
c1 = Counter()
c2 = Counter()
Counter.show_count()