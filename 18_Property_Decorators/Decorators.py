"""
    Assignment 18:
    Create a class Product with a private attribute _price. 
    Use @property to get the price, @price.setter to update it, 
    and @price.deleter to delete it.
"""

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price."""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price (with validation)."""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        print(f"Setting price to {value}...")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price."""
        print("Deleting price...")
        del self._price


# Test the Product class
product = Product(100)

# Get price (uses @property)
print(product.price)  # Output: Getting price... → 100

# Set price (uses @price.setter)
product.price = 150   # Output: Setting price to 150...

# Try setting invalid price
try:
    product.price = -50  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Price cannot be negative!

# Delete price (uses @price.deleter)
del product.price      # Output: Deleting price...

# Verify deletion
try:
    print(product.price)  # Raises AttributeError
except AttributeError:
    print("Price attribute deleted!")  # Output: Price attribute deleted!