# account_operators.py - Solution
# BankAccount with operator overloading

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


# Test code
if __name__ == "__main__":
    acc1 = BankAccount("Alice", 500)
    acc2 = BankAccount("Bob", 300)
    combined = acc1 + acc2
    print(f"Combined: {combined}")
    print(f"Alice > Bob: {acc1 > acc2}")
    print(f"Alice == Bob: {acc1 == acc2}")
