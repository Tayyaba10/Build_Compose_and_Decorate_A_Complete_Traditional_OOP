"""
Create a class Car with a public variable brand and a public method start(). 
Instantiate the class and access both from outside the class.
"""

# Defining the Car class
class Car:
    
    # Constructor to initialize the brand of the car
    def __init__(self, brand):
        self.brand = brand  # Public variable
        
    def start_car(self):
        # Method to start the car
        print(f"The {self.brand} car has started.")
        
# Creating an instance of the Car class
my_car = Car("Corolla")
# Accessing the public variable brand
print(f"Car Brand: {my_car.brand}")
# Calling the public method start_car
my_car.start_car()