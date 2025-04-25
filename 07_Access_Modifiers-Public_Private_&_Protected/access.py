""" 
    Assignment 07:
    Create a class Employee with:

    a public variable name,

    a protected variable _salary, and

    a private variable __ssn.

    Try accessing all three variables from an object of the class and document what happens.
    
"""
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private

    def display_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)

# Create object
emp = Employee("Leen", 70000, "123-654-9876")

# Accessing variables from outside the class
print("Outside class:")
print("Name:", emp.name)           # ✅ Public - Accessible

print("Salary:", emp._salary)      # ⚠️ Protected - Accessible, but discouraged

try:
    print("SSN:", emp.__ssn)       # ❌ Private - Raises AttributeError
except AttributeError as e:
    print("SSN: Cannot access directly:", e)

# Access private variable via name mangling (not recommended but possible)
print("Accessing SSN using name mangling:", emp._Employee__ssn)

# Optional: Show internal method accessing all variables
print("\nCalling method inside the class:")
emp.display_info()