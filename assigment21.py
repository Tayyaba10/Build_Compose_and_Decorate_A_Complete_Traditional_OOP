"""
Create a class Countdown that takes a start number. Implement __iter__() 
and __next__() to make the object iterable in a for-loop, counting down to 0.
"""

class Countdown():
    
    def __init__(self,start):
        self.current = start
        
    #__iter__() method    
    def __iter__(self):
        return self
    
    #__next__() method
    def __next__(self):
        # Check if the countdown is finished
        if self.current < 0:
            # Raise StopIteration to signal the end of the iteration
            raise StopIteration
        else:
            # Return the current value and decrement it
            value = self.current
            self.current -= 1
            return value
        
user = int(input("Enter a number to start countdown: "))        
c = Countdown(user)
# Using the Countdown class in a for-loop
for i in c:
    # This will print numbers from 10 to 0
    print(i)
