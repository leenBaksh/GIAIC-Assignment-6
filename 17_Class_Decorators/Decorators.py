"""
    Assignment 17:
    Create a class decorator add_greeting that modifies a class to 
    add a greet() method returning "Hello from Decorator!". 
    Apply it to a class Person.
"""


def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Add the greet() method to the class
    return cls  # Return the modified class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test
person = Person("Leena")
print(person.greet())  # Output: "Hello from Decorator!"

