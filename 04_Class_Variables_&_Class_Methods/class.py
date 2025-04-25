"""
Assignment:
Create a class Bank with a class variable bank_name. Add a class method 
change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

"""

class Bank:
    bank_name = "National Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Creating instances
acc1 = Bank("Leen")
acc2 = Bank("Affu")

# Display before changing bank name
print("Before changing bank name:")
acc1.display()
acc2.display()

# Change the bank name using class method
Bank.change_bank_name("World Wide Bank")

# Display after changing bank name
print("\nAfter changing bank name:")
acc1.display()
acc2.display()      