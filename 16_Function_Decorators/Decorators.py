"""
    Assignment 16:
    Write a decorator function log_function_call that prints "Function is being 
    called" before a function executes. Apply it to a function say_hello().
"""
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")  # Log before execution
        return func(*args, **kwargs)      # Call the original function
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Test
say_hello()