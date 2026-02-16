# Exercise 4: Raising Exceptions

def validate_age(age):
    """Validate age and raise exceptions for invalid values"""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be greater than 150")

    print(f"Age {age} is valid")
    return True

def validate_password(password):
    """Validate password strength and raise exceptions for weak passwords"""
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")

    print("Password is strong enough")
    return True

def withdraw_money(balance, amount):
    """Withdraw money with validation, raising exceptions for invalid operations"""
    if not isinstance(amount, (int, float)):
        raise TypeError("Withdrawal amount must be a number")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive")
    if amount > balance:
        raise ValueError(f"Insufficient funds. Balance: {balance}, Requested: {amount}")

    new_balance = balance - amount
    print(f"Successfully withdrew {amount}. New balance: {new_balance}")
    return new_balance

# Test code
if __name__ == "__main__":
    print("=== Raising Exceptions Tests ===\n")

    # Test validate_age
    test_ages = [25, -5, "twenty", 200]
    for age in test_ages:
        try:
            validate_age(age)
        except (TypeError, ValueError) as e:
            print(f"Age validation error for {age}: {e}")
        print()

    # Test validate_password
    test_passwords = ["Strong123", "weak", "nouppercase123", "NOLOWERCASE123", "NoDigits"]
    for pwd in test_passwords:
        try:
            validate_password(pwd)
        except ValueError as e:
            print(f"Password validation error for '{pwd}': {e}")
        print()

    # Test withdraw_money
    balance = 1000
    withdrawals = [100, -50, "fifty", 1500, 200]
    for amount in withdrawals:
        try:
            balance = withdraw_money(balance, amount)
        except (TypeError, ValueError) as e:
            print(f"Withdrawal error for {amount}: {e}")
        print(f"Current balance: {balance}\n")
