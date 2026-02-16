# savings_account.py
# TODO: Create SavingsAccount class inheriting from BankAccount

class BankAccount:
    """
    Base BankAccount class (copy from previous exercises)
    """

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} to {self.account_holder}'s account.")
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds or invalid amount.")
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount({self.account_holder}, ${self.balance:.2f})"


class SavingsAccount(BankAccount):
    """
    TODO: SavingsAccount inherits from BankAccount
    Add interest functionality and override methods
    """

    def __init__(self, account_holder, balance=0.0, interest_rate=0.02):
        """
        TODO: Call super().__init__ and initialize interest_rate
        """
        pass

    # TODO: Implement calculate_interest

    # TODO: Implement apply_interest

    # TODO: Override withdraw to add fee

    # TODO: Override __str__ to include interest rate


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     savings = SavingsAccount("Alice", 1000, 0.03)
#     savings.apply_interest()
#     savings.withdraw(50)
