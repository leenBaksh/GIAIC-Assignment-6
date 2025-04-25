"""  
Assignment 01:
Create a class Student with attributes name and marks. Use the self keyword to 
initialize these values via a constructor. Add a method display() that prints 
student details.

"""	

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        
student1 = Student("Leen", 25)
student1.display()