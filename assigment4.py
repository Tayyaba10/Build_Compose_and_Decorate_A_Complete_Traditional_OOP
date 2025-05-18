"""
Create a class Bank with a class variable bank_name.
Add a class method change_bank_name(cls, name) that allows 
changing the bank name. Show that it affects all instances.
"""
# Bank class with a class variable and a class method to change the bank name
class Bank():
    # Class variable
    bank_name = "State Bank Of Pakistan"
    
    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to: {cls.bank_name}") 
        
# Creating instances of the Bank class
bank1 = Bank()
print(f"Bank Name: {Bank.bank_name}")  # Output: State Bank Of Pakistan
Bank.change_bank_name("Meezan Bank")  # Changing the bank name

