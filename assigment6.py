"""
Create a class Logger that prints a message when an object is 
created (constructor) and another message when it is destroyed (destructor).
"""

# Define the Logger class
class Logger():
        def __init__(self):
                
                print("Logger object created.")
         
        def __del__(self):
               
                print("Logger object destroyed.")

# Test the Logger class
logger = Logger()  # Output: Logger object created.
del Logger  # Output: Logger object destroyed.