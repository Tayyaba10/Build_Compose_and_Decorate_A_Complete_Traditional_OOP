"""
Create a class TemperatureConverter with a static method 
celsius_to_fahrenheit(c) that returns the Fahrenheit value.
"""

# Define the TemperatureConverter class
class TemperatureConverter():
    
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
   
    def celsius_to_fahrenheit(celsius):
        # The formula for conversion is (C * 9/5) + 32
        return (celsius * 9/5) + 32
 
# Ask the user for input temperature in celsius  
celsius_input = float(input("Enter temperature in Celsius: "))   

# Create an instance of the TemperatureConverter class
temp = TemperatureConverter.celsius_to_fahrenheit(celsius_input)
print(f"Temperature in Fehrenheit: {temp:.2f} F.")