# account_strings.py
# TODO: Implement string representations for BankAccount

class BankAccount:
    """
    BankAccount with proper string representations.
    TODO: Implement __str__ and __repr__
    """

    def __init__(self, account_holder, balance=0.0, account_number=None):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number or f"ACC{hash(self):06X}"

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

    # TODO: Implement __str__ (user-friendly)

    # TODO: Implement __repr__ (developer format)


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     acc = BankAccount("John", 123.45)
#     print(acc)  # Uses __str__
#     print(repr(acc))  # Uses __repr__
