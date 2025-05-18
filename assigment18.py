"""
Create a class Product with a private attribute _price. 
Use @property to get the price, @price.setter to update it, 
and @price.deleter to delete it.
"""

class Product:
    def __init__(self,_price):
        self._price = _price
    
    # Getter for price    
    @property
    def price(self):
        return self._price
    
    # Setter for price
    @price.setter
    def price(self, new_price):
        self._price = new_price   
         
    # Deleter for price
    @price.deleter
    def price(self):
        del self._price
       
p = Product(1000)
print(f"Price: {p.price}")
# Update the price
p.price = 2000
# Updating the price
print(f"Updated Price: {p.price}")
# Deleting the price
del p.price
