# premium_account.py
# TODO: Create Rewardable mixin and PremiumAccount with multiple inheritance

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
    TODO: Implement Rewardable mixin class
    """

    def __init__(self, rewards_points=0):
        """
        TODO: Initialize rewards_points
        """
        pass

    # TODO: Implement earn_points

    # TODO: Implement redeem_points

    # TODO: Implement get_rewards_balance


class PremiumAccount(BankAccount, Rewardable):
    """
    TODO: PremiumAccount inherits from BankAccount and Rewardable
    """

    def __init__(self, account_holder, balance=0.0, rewards_points=0, monthly_fee=9.99):
        """
        TODO: Call both parent __init__ methods
        """
        pass

    # TODO: Override deposit to earn points

    # TODO: Override withdraw to earn points

    # TODO: Implement apply_monthly_fee

    # TODO: Override __str__ to show points and fee


# Test code (uncomment when ready)
# if __name__ == "__main__":
#     premium = PremiumAccount("Charlie", 500, 50, 9.99)
#     premium.deposit(200)
#     premium.redeem_points(30)
#     premium.apply_monthly_fee()
