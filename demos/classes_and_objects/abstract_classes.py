from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def add_interest(self):
        pass

class SavingsAccount(BankAccount):
    def add_interest(self):
        # Example: 5% interest
        self.balance += self.balance * 0.05

class CurrentAccount(BankAccount):
    def add_interest(self):
        # Example: No interest for current accounts
        pass

# Example usage:
savings = SavingsAccount(1000)
savings.add_interest()
print(f"Savings Account Balance: {savings.balance}")

current = CurrentAccount(1000)
current.add_interest()
print(f"Current Account Balance: {current.balance}")