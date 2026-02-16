# account_with_statics.py
# TODO: Extend BankAccount with static and class methods

class BankAccount:
    """
    BankAccount with static and class methods.
    TODO: Add class variable and required methods
    """

    # TODO: Add class variable total_accounts

    def __init__(self, account_holder, initial_balance=0.0):
        # TODO: Initialize and increment total_accounts
        pass

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

    # TODO: Add @classmethod get_total_accounts

    # TODO: Add @classmethod create_account

    # TODO: Add @staticmethod is_valid_amount

    # TODO: Add @staticmethod format_currency


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     acc1 = BankAccount("Alice", 500)
#     acc2 = BankAccount.create_account("Bob", 300)
#     print(BankAccount.get_total_accounts())
#     print(BankAccount.is_valid_amount(100))
#     print(BankAccount.format_currency(123.45))
