"""
Assignment:
Create a class Car with a public variable brand and a public method start(). 
Instantiate the class and access both from outside the class.

"""

class Car:
    def __init__ (self, brand): 
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting")

car = Car("BMW")
car.start()
my_car = Car("Audi")
my_car.start()

print(car.brand)
print("Car Brand:",my_car.brand)
