# basic_account.py
# TODO: Implement a basic BankAccount class

class BankAccount:
    """
    A simple BankAccount class.
    TODO: Implement the required methods
    """

    def __init__(self, account_holder, initial_balance=0.0):
        """
        TODO: Initialize account_holder and balance
        """
        pass

    def deposit(self, amount):
        """
        TODO: Add amount to balance if amount > 0
        Print deposit message
        """
        pass

    def withdraw(self, amount):
        """
        TODO: Subtract amount from balance if amount > 0 and sufficient funds
        Print withdrawal message
        """
        pass

    def get_balance(self):
        """
        TODO: Return current balance
        """
        pass


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     account = BankAccount("John Doe", 100.0)
#     account.deposit(50.0)
#     account.withdraw(30.0)
#     print(account.get_balance())
