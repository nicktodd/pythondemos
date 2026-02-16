# Exercise 5: Custom Exceptions

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds for a transaction"""

    def __init__(self, balance, amount, message="Insufficient funds for transaction"):
        self.balance = balance
        self.amount = amount
        self.message = f"{message}. Balance: {balance}, Required: {amount}"
        super().__init__(self.message)

class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid"""

    def __init__(self, amount, message="Invalid transaction amount"):
        self.amount = amount
        self.message = f"{message}: {amount}"
        super().__init__(self.message)

class AccountNotFoundError(Exception):
    """Raised when account is not found"""

    def __init__(self, account_id, message="Account not found"):
        self.account_id = account_id
        self.message = f"{message}: {account_id}"
        super().__init__(self.message)

class BankAccount:
    """Simple bank account with custom exceptions"""

    def __init__(self, account_id, initial_balance=0):
        if initial_balance < 0:
            raise InvalidAmountError(initial_balance, "Initial balance cannot be negative")
        self.account_id = account_id
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "Deposit amount must be positive")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount, "Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance")

        # Withdraw from current account
        self.withdraw(amount)
        # Deposit to target account
        target_account.deposit(amount)
        print(f"Transferred {amount} to account {target_account.account_id}")

def find_account(accounts, account_id):
    """Find account by ID, raise custom exception if not found"""
    for account in accounts:
        if account.account_id == account_id:
            return account
    raise AccountNotFoundError(account_id)

# Test code
if __name__ == "__main__":
    print("=== Custom Exceptions Tests ===\n")

    # Create accounts
    accounts = []
    try:
        acc1 = BankAccount("ACC001", 1000)
        acc2 = BankAccount("ACC002", 500)
        accounts.extend([acc1, acc2])
        print("Accounts created successfully\n")
    except InvalidAmountError as e:
        print(f"Account creation error: {e}\n")

    # Test deposits and withdrawals
    try:
        acc1.deposit(200)
        acc1.withdraw(150)
        acc1.withdraw(2000)  # Should fail
    except (InvalidAmountError, InsufficientFundsError) as e:
        print(f"Transaction error: {e}\n")

    # Test transfers
    try:
        acc1.transfer(acc2, 100)
        acc1.transfer("not_an_account", 50)  # Should fail
    except (TypeError, InvalidAmountError, InsufficientFundsError) as e:
        print(f"Transfer error: {e}\n")

    # Test account lookup
    try:
        found = find_account(accounts, "ACC001")
        print(f"Found account: {found.account_id}")
        find_account(accounts, "NONEXISTENT")  # Should fail
    except AccountNotFoundError as e:
        print(f"Lookup error: {e}")
