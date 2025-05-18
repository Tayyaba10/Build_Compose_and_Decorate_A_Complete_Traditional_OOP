"""
Write a decorator function log_function_call that prints 
"Function is being called" before a function executes. 
Apply it to a function say_hello().
"""

# This is a simple decorator that logs when a function is called.
def log_function_call(func):
    
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Decorate the say_hello function with the log_function_call decorator
@log_function_call
def say_hello():
    print("Hello, World!")

# Test the decorator
if __name__ == "__main__":
    say_hello()