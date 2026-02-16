# str_repr.py
# Demonstrating __str__ and __repr__ methods in Python using BankAccount

class BankAccount:
    """
    BankAccount class demonstrating __str__ and __repr__.
    """

    def __init__(self, account_holder, balance=0.0, account_number=None):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number or f"ACC{hash(self):06X}"  # Simple account number

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

    def __str__(self):
        """
        __str__ method: Returns a user-friendly string representation.
        This is called by str() and print() functions.
        Should be readable and informative for end users.
        """
        return f"Bank Account: {self.account_holder} (#{self.account_number}) - Balance: ${self.balance:.2f}"

    def __repr__(self):
        """
        __repr__ method: Returns an unambiguous string representation.
        This is called by repr() and in interactive sessions.
        Should be detailed enough to recreate the object if possible.
        Used for debugging and development.
        """
        return f"BankAccount(account_holder='{self.account_holder}', balance={self.balance}, account_number='{self.account_number}')"


# Demo usage
if __name__ == "__main__":
    account = BankAccount("John Smith", 1234.56)

    print("Using print() - calls __str__:")
    print(account)

    print("\nUsing str() - calls __str__:")
    print(str(account))

    print("\nUsing repr() - calls __repr__:")
    print(repr(account))

    print("\nIn a list - repr is used:")
    accounts = [account, BankAccount("Jane Doe", 789.01)]
    print(accounts)

    print("\nRepr can be used to recreate object:")
    # Using eval is dangerous in real code, but for demo:
    recreated = eval(repr(account))
    print(f"Original: {account}")
    print(f"Recreated: {recreated}")
    print(f"Are they equal? {account.balance == recreated.balance and account.account_holder == recreated.account_holder}")
