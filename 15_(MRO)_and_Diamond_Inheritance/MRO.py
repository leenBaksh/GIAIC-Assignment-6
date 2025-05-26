"""
    Assignment 15:
    
    Create four classes:

    . A with a method show(),

    . B and C that inherit from A and override show(),

    . D that inherits from both B and C.

    Create an object of D and call show() to observe MRO.
"""

class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass  # Inherits from both B and C

# Create an object of D and call show()
d = D()
d.show()  # Which show() is called?



# Print the Method Resolution Order (MRO)
print(D.__mro__)