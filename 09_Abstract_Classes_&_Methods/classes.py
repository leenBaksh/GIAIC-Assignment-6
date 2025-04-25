""" 
Assignment 09:
Use the abc module to create an abstract class Shape with an abstract method area(). 
Inherit a class Rectangle that implements area().

"""

from abc import ABC, abstractmethod

class Shape(ABC):  
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10

rectangle = Rectangle()
print(rectangle.area())