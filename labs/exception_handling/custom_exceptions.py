# Exercise 5: Custom Exceptions

# TODO: Create custom exception classes: InsufficientFundsError, InvalidAmountError, AccountNotFoundError

# TODO: Create BankAccount class with deposit, withdraw, transfer methods

# TODO: Implement find_account function

# Test code (uncomment to test)
# try:
#     account = BankAccount("ACC001", 1000)
#     account.deposit(500)
#     account.withdraw(2000)  # Should raise InsufficientFundsError
# except InsufficientFundsError as e:
#     print(f"Funds error: {e}")

# try:
#     account.deposit(-100)  # Should raise InvalidAmountError
# except InvalidAmountError as e:
#     print(f"Amount error: {e}")
