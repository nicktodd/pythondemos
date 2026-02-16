# multiple_inheritance.py
# Demonstrating multiple inheritance in Python using BankAccount, Rewardable, and PremiumAccount

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
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount({self.account_holder}, ${self.balance:.2f})"


class Rewardable:
    """
    Mixin class for accounts that can earn rewards.
    """

    def __init__(self, rewards_points=0):
        self.rewards_points = rewards_points

    def earn_points(self, amount):
        """
        Earn reward points based on transaction amount.
        1 point per $10 spent/deposited.
        """
        points = amount // 10
        self.rewards_points += points
        print(f"Earned {points} reward points. Total points: {self.rewards_points}")
        return points

    def redeem_points(self, points):
        """
        Redeem reward points for cash back.
        100 points = $1 cash back.
        """
        if points <= self.rewards_points:
            cash_back = points / 100
            self.rewards_points -= points
            print(f"Redeemed {points} points for ${cash_back:.2f} cash back.")
            return cash_back
        else:
            print("Insufficient reward points.")
            return 0

    def get_rewards_balance(self):
        return self.rewards_points


class PremiumAccount(BankAccount, Rewardable):
    """
    PremiumAccount inherits from both BankAccount and Rewardable.
    Demonstrates multiple inheritance.
    """

    def __init__(self, account_holder, balance=0.0, rewards_points=0, monthly_fee=9.99):
        # Initialize both parent classes
        BankAccount.__init__(self, account_holder, balance)
        Rewardable.__init__(self, rewards_points)
        self.monthly_fee = monthly_fee

    def deposit(self, amount):
        """
        Override deposit to earn reward points.
        """
        result = super().deposit(amount)  # Call BankAccount's deposit
        self.earn_points(amount)  # Earn points from Rewardable
        return result

    def withdraw(self, amount):
        """
        Override withdraw to earn reward points (for spending).
        """
        result = super().withdraw(amount)
        if result < self.balance:  # Only if withdrawal was successful
            self.earn_points(amount)
        return result

    def apply_monthly_fee(self):
        """
        Apply monthly fee for premium account.
        """
        if self.balance >= self.monthly_fee:
            self.balance -= self.monthly_fee
            print(f"Applied monthly fee: ${self.monthly_fee:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds for monthly fee.")

    def __str__(self):
        """
        Override __str__ to include rewards and fee info.
        """
        return f"PremiumAccount({self.account_holder}, ${self.balance:.2f}, {self.rewards_points} points, Fee: ${self.monthly_fee:.2f})"


# Demo usage
if __name__ == "__main__":
    # Create a premium account
    premium = PremiumAccount("Charlie", 500.0, 50, 9.99)
    print("Premium Account:")
    print(premium)

    # Deposit money (earns points)
    premium.deposit(200)

    # Withdraw money (earns points)
    premium.withdraw(50)

    # Redeem points
    cash_back = premium.redeem_points(30)
    premium.balance += cash_back  # Add cash back to balance

    # Apply monthly fee
    premium.apply_monthly_fee()

    print("\nFinal state:")
    print(premium)

    # Demonstrate method resolution order (MRO)
    print(f"\nMethod Resolution Order: {PremiumAccount.__mro__}")

    # Check if instance of both classes
    print(f"Is PremiumAccount a BankAccount? {isinstance(premium, BankAccount)}")
    print(f"Is PremiumAccount Rewardable? {isinstance(premium, Rewardable)}")
