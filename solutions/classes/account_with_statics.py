# account_with_statics.py - Solution
# BankAccount with static and class methods

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


# Test code
if __name__ == "__main__":
    acc1 = BankAccount("Alice", 500)
    acc2 = BankAccount.create_account("Bob", 300)
    print(f"Total accounts: {BankAccount.get_total_accounts()}")
    print(f"Is 100 valid? {BankAccount.is_valid_amount(100)}")
    print(f"Formatted currency: {BankAccount.format_currency(123.45)}")
