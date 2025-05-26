"""
    Assignment 20:
    Create a custom exception InvalidAgeError. 
    Write a function check_age(age) that raises this exception 
    if age < 18. Handle it with try...except.
"""

# 1. Define the custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(f"{message} (got {age})")

# 2. Function that raises the exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid!")

# 3. Test with try-except
try:
    check_age(15)  # This will raise InvalidAgeError
except InvalidAgeError as e:
    print(f"Error: {e}")  # Handle the custom exception

# Successful case
try:
    check_age(25)  # This will pass
except InvalidAgeError:
    print("This won't execute")