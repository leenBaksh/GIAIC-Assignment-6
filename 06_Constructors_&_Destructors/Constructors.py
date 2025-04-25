"""
    Assignment 06:
    Create a class Logger that prints a message when an object is created (constructor) and another message
    when it is destroyed (destructor).
    
"""

class Logger:
    def __init__(self, message):
        self.message = message
        print(self.message)

    def __del__(self):
        print("🔴 Logger instance is being cleaned up.")

logger = Logger("🟢 A new Logger instance has been initialized.")
del logger