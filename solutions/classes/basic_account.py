# basic_account.py - Solution
# Basic BankAccount class implementation

class BankAccount:
    """
    A simple BankAccount class to demonstrate basic class concepts.
    """

    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initialize a new bank account.

        Args:
            account_holder (str): Name of the account holder
            initial_balance (float): Starting balance, defaults to 0.0
        """
        self.account_holder = account_holder  # Instance variable for account holder name
        self.balance = initial_balance        # Instance variable for current balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit

        Returns:
            float: New balance after deposit
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Returns:
            float: New balance after withdrawal
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount.")
        return self.balance

    def get_balance(self):
        """
        Get the current balance.

        Returns:
            float: Current balance
        """
        return self.balance


# Test code
if __name__ == "__main__":
    account = BankAccount("John Doe", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    print(f"Final balance: ${account.get_balance():.2f}")
