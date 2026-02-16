# inheritance.py
# Demonstrating inheritance in Python using BankAccount and SavingsAccount

class BankAccount:
    """
    Base BankAccount class.
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
    SavingsAccount inherits from BankAccount.
    Adds interest rate and methods to calculate/apply interest.
    """

    def __init__(self, account_holder, balance=0.0, interest_rate=0.02):
        """
        Initialize SavingsAccount with interest rate.
        Calls parent __init__ using super().
        """
        super().__init__(account_holder, balance)  # Call parent constructor
        self.interest_rate = interest_rate  # Additional attribute

    def calculate_interest(self):
        """
        Calculate interest based on current balance and rate.
        """
        return self.balance * self.interest_rate

    def apply_interest(self):
        """
        Apply interest to the account balance.
        """
        interest = self.calculate_interest()
        self.balance += interest
        print(f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount):
        """
        Override withdraw method to add a small fee for savings account.
        """
        fee = 1.00  # Small withdrawal fee
        total_amount = amount + fee
        if total_amount <= self.balance:
            self.balance -= total_amount
            print(f"Withdrew ${amount:.2f} plus ${fee:.2f} fee. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds including fee.")
        return self.balance

    def __str__(self):
        """
        Override __str__ to include interest rate.
        """
        return f"SavingsAccount({self.account_holder}, ${self.balance:.2f}, {self.interest_rate*100:.1f}%)"


# Demo usage
if __name__ == "__main__":
    # Create a regular bank account
    regular_account = BankAccount("Alice", 1000.0)
    print("Regular Account:")
    print(regular_account)
    regular_account.deposit(200)
    regular_account.withdraw(100)

    print("\n" + "="*50 + "\n")

    # Create a savings account
    savings_account = SavingsAccount("Bob", 1000.0, 0.03)  # 3% interest
    print("Savings Account:")
    print(savings_account)

    # Calculate interest
    interest = savings_account.calculate_interest()
    print(f"Annual interest: ${interest:.2f}")

    # Apply interest
    savings_account.apply_interest()

    # Withdraw with fee
    savings_account.withdraw(50)

    print("\nFinal balances:")
    print(regular_account)
    print(savings_account)
