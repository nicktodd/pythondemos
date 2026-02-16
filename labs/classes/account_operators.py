# account_operators.py
# TODO: Add operator overloading to BankAccount

class BankAccount:
    """
    BankAccount with operator overloading.
    TODO: Implement the required operators
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

    # TODO: Implement __add__

    # TODO: Implement __sub__

    # TODO: Implement __eq__

    # TODO: Implement __lt__, __le__, __gt__, __ge__

    # TODO: Implement __str__


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     acc1 = BankAccount("Alice", 500)
#     acc2 = BankAccount("Bob", 300)
#     combined = acc1 + acc2
#     print(acc1 > acc2)
#     print(str(acc1))
