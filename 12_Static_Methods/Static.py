"""
    Assignment 12:
    Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
    that returns the Fahrenheit value.
"""

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """Convert temperature from Celsius to Fahrenheit.
        
        Args:
            c (float): Temperature in Celsius.
            
        Returns:
            float: Temperature in Fahrenheit.
        """
        return (c * 9/5) + 32
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(100)
print(fahrenheit)  # Output: 212.0    