# operator_overloading.py
# Demonstrating operator overloading in Python using BankAccount

class BankAccount:
    """
    BankAccount class with operator overloading.
    """

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

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

    def __add__(self, other):
        """
        Overload + operator to add balances of two accounts.
        Returns a new account with combined balance.
        """
        if isinstance(other, BankAccount):
            combined_balance = self.balance + other.balance
            return BankAccount(f"{self.account_holder} + {other.account_holder}", combined_balance)
        elif isinstance(other, (int, float)):
            # Allow adding a number to balance
            return BankAccount(self.account_holder, self.balance + other)
        return NotImplemented

    def __sub__(self, other):
        """
        Overload - operator to subtract balances or amounts.
        """
        if isinstance(other, BankAccount):
            diff_balance = self.balance - other.balance
            return BankAccount(f"{self.account_holder} - {other.account_holder}", diff_balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.account_holder, self.balance - other)
        return NotImplemented

    def __eq__(self, other):
        """
        Overload == operator to compare balances.
        """
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        return False

    def __lt__(self, other):
        """
        Overload < operator for balance comparison.
        """
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    def __le__(self, other):
        """
        Overload <= operator.
        """
        if isinstance(other, BankAccount):
            return self.balance <= other.balance
        return NotImplemented

    def __gt__(self, other):
        """
        Overload > operator.
        """
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return NotImplemented

    def __ge__(self, other):
        """
        Overload >= operator.
        """
        if isinstance(other, BankAccount):
            return self.balance >= other.balance
        return NotImplemented

    def __str__(self):
        """
        String representation for end users.
        """
        return f"Account({self.account_holder}, Balance: ${self.balance:.2f})"

    def __repr__(self):
        """
        Official string representation for developers/debugging.
        """
        return f"BankAccount('{self.account_holder}', {self.balance})"


# Demo usage
if __name__ == "__main__":
    account1 = BankAccount("Alice", 500.0)
    account2 = BankAccount("Bob", 300.0)
    account3 = BankAccount("Charlie", 500.0)

    print("Original accounts:")
    print(account1)
    print(account2)
    print(account3)

    # Add two accounts
    combined = account1 + account2
    print(f"\nCombined account: {combined}")

    # Add number to account
    account1_plus_100 = account1 + 100
    print(f"Alice + 100: {account1_plus_100}")

    # Subtract accounts
    diff = account1 - account2
    print(f"Alice - Bob: {diff}")

    # Compare accounts
    print(f"\nAlice == Charlie (same balance): {account1 == account3}")
    print(f"Alice == Bob: {account1 == account2}")
    print(f"Alice > Bob: {account1 > account2}")
    print(f"Bob < Alice: {account2 < account1}")
