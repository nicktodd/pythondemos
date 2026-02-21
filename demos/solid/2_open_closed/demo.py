# Open/Closed Principle (OCP)
# Software entities should be open for extension but closed for modification

from abc import ABC, abstractmethod

# BAD: Adding new discount types requires modifying existing code
class BadDiscountCalculator:
    def calculate_discount(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.0  # No discount
        elif customer_type == "premium":
            return amount * 0.1  # 10% discount
        elif customer_type == "vip":
            return amount * 0.2  # 20% discount
        # Adding a new customer type requires modifying this method!
        else:
            return 0


# GOOD: New discount types can be added without modifying existing code
class DiscountStrategy(ABC):
    """Abstract base class - defines the contract"""
    @abstractmethod
    def calculate_discount(self, amount):
        pass


class NoDiscount(DiscountStrategy):
    """Regular customers - no discount"""
    def calculate_discount(self, amount):
        return 0


class PremiumDiscount(DiscountStrategy):
    """Premium customers - 10% discount"""
    def calculate_discount(self, amount):
        return amount * 0.1


class VIPDiscount(DiscountStrategy):
    """VIP customers - 20% discount"""
    def calculate_discount(self, amount):
        return amount * 0.2


class StudentDiscount(DiscountStrategy):
    """NEW: Student customers - 15% discount
    Added without modifying any existing code!"""
    def calculate_discount(self, amount):
        return amount * 0.15


class DiscountCalculator:
    """Closed for modification, open for extension"""
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
    
    def calculate_final_price(self, amount):
        discount = self.discount_strategy.calculate_discount(amount)
        return amount - discount


# Usage
if __name__ == "__main__":
    print("=== Bad Example ===")
    bad_calc = BadDiscountCalculator()
    print(f"Regular customer (£100): £{100 - bad_calc.calculate_discount('regular', 100):.2f}")
    print(f"Premium customer (£100): £{100 - bad_calc.calculate_discount('premium', 100):.2f}")
    print(f"VIP customer (£100): £{100 - bad_calc.calculate_discount('vip', 100):.2f}")
    # To add student discount, we'd need to modify the BadDiscountCalculator class!
    
    print("\n=== Good Example ===")
    amount = 100
    
    regular_calc = DiscountCalculator(NoDiscount())
    print(f"Regular customer (£{amount}): £{regular_calc.calculate_final_price(amount):.2f}")
    
    premium_calc = DiscountCalculator(PremiumDiscount())
    print(f"Premium customer (£{amount}): £{premium_calc.calculate_final_price(amount):.2f}")
    
    vip_calc = DiscountCalculator(VIPDiscount())
    print(f"VIP customer (£{amount}): £{vip_calc.calculate_final_price(amount):.2f}")
    
    # NEW: Student discount added without modifying existing classes!
    student_calc = DiscountCalculator(StudentDiscount())
    print(f"Student customer (£{amount}): £{student_calc.calculate_final_price(amount):.2f}")
