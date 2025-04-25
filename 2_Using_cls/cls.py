""" 
Assignment 02:
Create a class Counter that keeps track of how many objects have been created. Use a class variable and
a class method with cls to manage and display the count.

"""

class Counter:
    count = 0

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")
        

counter1 = Counter()
counter2 = Counter()

Counter.display_count()