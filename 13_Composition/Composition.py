"""
    Assignment 13:
    Create a class Engine and a class Car. Use composition by passing an Engine 
    object to the Car class during initialization. Access a method of the Engine 
    class via the Car class.
"""

class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method

    def stop_car(self):
        print("Stopping the car...")
        self.engine.stop()   # Accessing Engine's method


# Usage
if __name__ == "__main__":
    engine = Engine()        # Create an Engine object
    car = Car(engine)        # Pass the Engine to the Car (composition)

    car.start_car()          # Output: "Starting the car..." -> "Engine started."
    car.stop_car()           # Output: "Stopping the car..." -> "Engine stopped."
