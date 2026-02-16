# static_methods.py
# Demonstrating static methods and class methods in Python using BankAccount

class BankAccount:
    """
    BankAccount class with static and class methods.
    """

    # Class variable to keep track of total accounts
    total_accounts = 0

    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_accounts += 1  # Increment class variable

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        """
        Class method to get the total number of accounts created.
        Class methods receive the class as the first parameter (cls).
        """
        return cls.total_accounts

    @classmethod
    def create_account(cls, account_holder, initial_balance=0.0):
        """
        Class method to create a new account.
        This is an alternative constructor.
        """
        return cls(account_holder, initial_balance)

    @staticmethod
    def is_valid_amount(amount):
        """
        Static method to check if an amount is valid (positive number).
        Static methods don't receive self or cls, they are utility functions.
        """
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def format_currency(amount):
        """
        Static method to format an amount as currency.
        """
        return f"${amount:.2f}"


# Demo usage
if __name__ == "__main__":
    # Create accounts using regular constructor
    account1 = BankAccount("Alice", 500.0)
    account2 = BankAccount("Bob", 300.0)

    # Create account using class method
    account3 = BankAccount.create_account("Charlie", 100.0)

    print(f"Total accounts created: {BankAccount.get_total_accounts()}")

    # Use static methods
    print(f"Is 50 a valid amount? {BankAccount.is_valid_amount(50)}")
    print(f"Is -10 a valid amount? {BankAccount.is_valid_amount(-10)}")
    print(f"Formatted currency: {BankAccount.format_currency(123.45)}")

    # Demonstrate on instances
    account1.deposit(100)
    print(f"Alice's balance: {BankAccount.format_currency(account1.get_balance())}")
