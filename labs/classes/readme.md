# Python Classes and Objects Lab

This lab will guide you through implementing key object-oriented programming concepts in Python using BankAccount examples. You'll build upon the concepts demonstrated in the `demos/classes_and_objects/` folder.

## Prerequisites

Before starting, review the demo files in `demos/classes_and_objects/` to understand the concepts:

- `basic_class.py` - Basic class structure
- `static_methods.py` - Static and class methods
- `operator_overloading.py` - Operator overloading
- `str_repr.py` - String representations
- `inheritance.py` - Single inheritance
- `multiple_inheritance.py` - Multiple inheritance

## Lab Structure

- **Starter files**: Located in `labs/classes/`
- **Solutions**: Located in `solutions/classes/` (check after completing exercises)
- **Your work**: Modify the starter files in `labs/classes/`

## Exercise 1: Basic BankAccount Class

**File**: `labs/classes/basic_account.py`

Implement a basic `BankAccount` class with the following requirements:

1. `__init__(self, account_holder, initial_balance=0.0)` - Initialize account holder name and balance
2. `deposit(self, amount)` - Add money to balance (only if amount > 0)
3. `withdraw(self, amount)` - Subtract money from balance (only if amount > 0 and sufficient funds)
4. `get_balance(self)` - Return current balance
5. Include appropriate print statements for transactions

**Test your implementation**:
```python
account = BankAccount("John Doe", 100.0)
account.deposit(50.0)  # Should print deposit message
account.withdraw(30.0)  # Should print withdrawal message
print(account.get_balance())  # Should print 120.0
```

## Exercise 2: Static and Class Methods

**File**: `labs/classes/account_with_statics.py`

Extend the BankAccount class with static and class methods:

1. Add a class variable `total_accounts` to track number of accounts created
2. `@classmethod get_total_accounts(cls)` - Return total accounts
3. `@classmethod create_account(cls, account_holder, initial_balance=0.0)` - Alternative constructor
4. `@staticmethod is_valid_amount(amount)` - Check if amount is positive number
5. `@staticmethod format_currency(amount)` - Format amount as currency string

**Test your implementation**:
```python
acc1 = BankAccount("Alice", 500)
acc2 = BankAccount.create_account("Bob", 300)
print(BankAccount.get_total_accounts())  # Should be 2
print(BankAccount.is_valid_amount(100))  # True
print(BankAccount.format_currency(123.45))  # "$123.45"
```

## Exercise 3: Operator Overloading

**File**: `labs/classes/account_operators.py`

Add operator overloading to the BankAccount class:

1. `__add__(self, other)` - Add balances or add number to balance
2. `__sub__(self, other)` - Subtract balances or subtract number from balance
3. `__eq__(self, other)` - Compare balances for equality
4. `__lt__(self, other)`, `__le__`, `__gt__`, `__ge__` - Comparison operators
5. `__str__(self)` - User-friendly string representation

**Test your implementation**:
```python
acc1 = BankAccount("Alice", 500)
acc2 = BankAccount("Bob", 300)
combined = acc1 + acc2  # New account with balance 800
print(acc1 > acc2)  # True
print(str(acc1))  # Should show account info
```

## Exercise 4: String Representations

**File**: `labs/classes/account_strings.py`

Implement proper string representations:

1. `__str__(self)` - User-friendly format: "Account: [holder] (#ID) - Balance: $[balance]"
2. `__repr__(self)` - Developer format for debugging/recreation

**Test your implementation**:
```python
acc = BankAccount("John", 123.45)
print(acc)  # Uses __str__
print(repr(acc))  # Uses __repr__
```

## Exercise 5: Inheritance

**File**: `labs/classes/savings_account.py`

Create a `SavingsAccount` class that inherits from `BankAccount`:

1. Add `interest_rate` parameter to `__init__`
2. `calculate_interest(self)` - Return interest amount (balance * rate)
3. `apply_interest(self)` - Add interest to balance
4. Override `withdraw` to add a $1.00 fee
5. Override `__str__` to include interest rate

**Test your implementation**:
```python
savings = SavingsAccount("Alice", 1000, 0.03)
savings.apply_interest()  # Balance becomes 1030
savings.withdraw(50)  # Balance becomes 979 (50 + 1 fee)
```

## Exercise 6: Multiple Inheritance

**File**: `labs/classes/premium_account.py`

Create a `Rewardable` mixin class and a `PremiumAccount` that inherits from both `BankAccount` and `Rewardable`:

**Rewardable class**:
1. `__init__(self, rewards_points=0)` - Initialize points
2. `earn_points(self, amount)` - Add points (1 point per $10)
3. `redeem_points(self, points)` - Convert points to cash back ($1 per 100 points)
4. `get_rewards_balance(self)` - Return current points

**PremiumAccount class**:
1. Inherits from `BankAccount` and `Rewardable`
2. `__init__` should call both parent `__init__` methods
3. Override `deposit` and `withdraw` to earn points
4. Add `apply_monthly_fee(self)` method ($9.99 fee)
5. Override `__str__` to show points and fee

**Test your implementation**:
```python
premium = PremiumAccount("Charlie", 500, 50, 9.99)
premium.deposit(200)  # Earns 20 points
premium.redeem_points(30)  # Gets $0.30 cash back
premium.apply_monthly_fee()  # Deducts $9.99
```

## Submission

1. Complete all exercises in the `labs/classes/` files
2. Test your implementations with the provided test cases
3. Compare your solutions with the completed versions in `solutions/classes/`
4. Run the demo files to see advanced examples

## Tips

- Start with Exercise 1 and build upon previous exercises
- Use the demo files as references, but implement your own versions
- Test frequently as you implement each method
- Pay attention to method signatures and return types
- Use `super()` when overriding inherited methods