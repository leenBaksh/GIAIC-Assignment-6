"""
    Assignment 19:
    Create a class Multiplier with an __init__() to set a factor. 
    Define a __call__() method that multiplies an input by the factor. 
    Test it with callable() and by calling the object like a function.
"""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Set the multiplication factor

    def __call__(self, x):
        """Multiply input x by the factor when the object is called like a function."""
        return x * self.factor

# Test the Multiplier class
multiply_by_3 = Multiplier(3)  # Create a multiplier with factor 3

# 1. Verify the object is callable
print("Is multiply_by_3 callable?", callable(multiply_by_3))  # Output: True

# 2. Call the object like a function
result = multiply_by_3(5)
print("5 multiplied by 3:", result)  # Output: 15

# 3. Create another multiplier and test it
multiply_by_10 = Multiplier(10)
print("7 multiplied by 10:", multiply_by_10(7))  # Output: 70