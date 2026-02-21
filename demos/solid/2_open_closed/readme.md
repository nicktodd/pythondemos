# Open/Closed Principle (OCP)

## Definition
**Software entities (classes, modules, functions) should be open for extension but closed for modification.**

You should be able to add new functionality without changing existing code. This is achieved through abstraction and polymorphism.

## The Problem

When you need to add new behavior:
- **Modify existing code**: Risks breaking what already works
- **Violates stability**: Tested code is changed and needs retesting
- **Coupling**: New features are tangled with old code
- **Fragile**: Every change risks introducing bugs

In the bad example, adding a new customer type (like "student") requires:
1. Modifying the `BadDiscountCalculator` class
2. Adding another `elif` branch
3. Retesting all existing discount logic

## The Solution

Use **abstraction** and **polymorphism**:
1. Define an abstract `DiscountStrategy` interface
2. Each discount type implements the interface
3. New discount types are added by creating new classes, not modifying existing ones

The `DiscountCalculator` is:
- **Closed for modification**: Its code never needs to change
- **Open for extension**: New strategies can be plugged in

## Benefits

1. **Stability**: Existing code remains unchanged and tested
2. **Flexibility**: New features added without risk to old ones
3. **Testability**: New strategies tested independently
4. **Maintainability**: Changes isolated to new code only
5. **Scalability**: Easy to add unlimited new discount types

## Strategy Pattern

This example uses the **Strategy Pattern**:
- Define a family of algorithms (discount strategies)
- Encapsulate each one in a class
- Make them interchangeable

The pattern makes the algorithm independent of clients that use it.

## Real-World Example

Think of payment methods in an online store:
- The checkout process (calculator) doesn't change
- You can add new payment methods (strategies) like:
  - Credit Card
  - PayPal
  - Apple Pay
  - Bitcoin (NEW!)
- Each new method doesn't require changing the checkout code

## When to Apply

Ask yourself: "If I need to add a new variation of this behavior, will I have to modify existing code?"

If yes, consider using abstraction (interfaces/abstract classes) to make the code open for extension.

## Run the Demo

```bash
python demo.py
```

Notice how the "student discount" was added without touching any existing classes!

## Key Takeaway

**"Open for extension, closed for modification"** means designing your code so that new features are added by writing new code, not by changing old code. This is the heart of maintainable, scalable software.
