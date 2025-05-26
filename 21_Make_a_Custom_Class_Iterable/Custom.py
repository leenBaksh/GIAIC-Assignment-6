"""
    Assignment 21:
    Create a class Countdown that takes a start number. 
    Implement __iter__() and __next__() to make the object 
    iterable in a for-loop, counting down to 0.
"""

class Countdown:
    def __init__(self, start):
        self.start = start + 1  # We add 1 because we decrement first in __next__

    def __iter__(self):
        return self  # Returns the iterator object itself

    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration  # Signal the end of iteration
        return self.start

# Test the Countdown
print("Countdown from 5:")
for num in Countdown(5):
    print(num, end=" ")  # Output: 5 4 3 2 1 0

print("\n\nCountdown from 3:")
for num in Countdown(3):
    print(num, end=" ")  # Output: 3 2 1 0