# SOLID Principles in Python

This directory contains simple, focused examples demonstrating each of the five SOLID principles of object-oriented design.

## What are SOLID Principles?

SOLID is an acronym for five design principles that make software more understandable, flexible, and maintainable:

1. **S**ingle Responsibility Principle (SRP)
2. **O**pen/Closed Principle (OCP)
3. **L**iskov Substitution Principle (LSP)
4. **I**nterface Segregation Principle (ISP)
5. **D**ependency Inversion Principle (DIP)

These principles were promoted by Robert C. Martin (Uncle Bob) and form the foundation of clean, maintainable object-oriented code.

## Directory Structure

```
solid/
├── 1_single_responsibility/
│   ├── demo.py          # Examples of SRP
│   └── readme.md        # Explanation of SRP
├── 2_open_closed/
│   ├── demo.py          # Examples of OCP
│   └── readme.md        # Explanation of OCP
├── 3_liskov_substitution/
│   ├── demo.py          # Examples of LSP
│   └── readme.md        # Explanation of LSP
├── 4_interface_segregation/
│   ├── demo.py          # Examples of ISP
│   └── readme.md        # Explanation of ISP
├── 5_dependency_inversion/
│   ├── demo.py          # Examples of DIP
│   └── readme.md        # Explanation of DIP
└── readme.md            # This file
```

## Quick Overview

### 1. Single Responsibility Principle
**One class, one job.** Each class should have only one reason to change.

**Example**: Separate `Employee` (data), `PayrollCalculator` (business logic), `EmployeeRepository` (persistence)

### 2. Open/Closed Principle
**Open for extension, closed for modification.** Add new features without changing existing code.

**Example**: Use `DiscountStrategy` abstraction to add new discount types without modifying the calculator

### 3. Liskov Substitution Principle
**Subtypes must be substitutable for their base types.** Derived classes should work anywhere the base class works.

**Example**: `Square` should NOT inherit from `Rectangle` if it breaks rectangle behavior

### 4. Interface Segregation Principle
**Don't force classes to implement methods they don't use.** Many small interfaces are better than one large interface.

**Example**: Separate `Workable`, `Eatable`, `Sleepable` instead of one `Worker` interface

### 5. Dependency Inversion Principle
**Depend on abstractions, not concretions.** High-level code should not depend on low-level implementation details.

**Example**: `NotificationService` depends on `MessageSender` abstraction, not concrete `EmailSender`

## Running the Examples

Each principle has its own directory with a runnable demo:

```bash
# Single Responsibility
python 1_single_responsibility/demo.py

# Open/Closed
python 2_open_closed/demo.py

# Liskov Substitution
python 3_liskov_substitution/demo.py

# Interface Segregation
python 4_interface_segregation/demo.py

# Dependency Inversion
python 5_dependency_inversion/demo.py
```

Each demo shows:
- **Bad Example**: Code that violates the principle
- **Good Example**: Code that follows the principle
- **Explanation**: Why the good example is better

## Why SOLID Matters

Following SOLID principles helps you:

1. **Write maintainable code**: Easy to understand and modify
2. **Reduce bugs**: Changes are isolated and predictable
3. **Enable testing**: Code is decoupled and mockable
4. **Improve reusability**: Components can be used in different contexts
5. **Support change**: New requirements don't break existing code
6. **Collaborate better**: Clear responsibilities and contracts

## When to Apply SOLID

SOLID principles are **guidelines**, not rules:

- Apply them when they improve design
- Use them to identify code smells
- Refactor toward SOLID as systems grow
- Don't over-engineer simple code
- Don't apply all principles everywhere
- Don't sacrifice clarity for principle adherence

**Start simple, refactor toward SOLID as complexity grows.**

## SOLID in Python

Python's dynamic nature affects how we apply SOLID:

- **Duck typing**: Interfaces are often implicit
- **ABC module**: Use for explicit interfaces/abstract classes
- **Multiple inheritance**: Supports Interface Segregation naturally
- **First-class functions**: Enables Strategy pattern easily
- **Dependency injection**: Simple with keyword arguments

The examples in this directory use Python idioms while demonstrating universal SOLID concepts.

## Learning Path

**Recommended order**:

1. **Start with SRP**: Easiest to understand and apply
2. **Then OCP**: Builds on SRP, introduces abstraction
3. **Then DIP**: Uses abstractions from OCP
4. **Then ISP**: Refines interface design from DIP
5. **Finally LSP**: Most subtle, requires understanding inheritance

## Common Patterns

SOLID principles enable design patterns:

- **SRP** → Separate concerns (MVC, Service Layer)
- **OCP** → Strategy, Template Method, Decorator patterns
- **LSP** → Proper inheritance, Polymorphism
- **ISP** → Role interfaces, Adapter pattern
- **DIP** → Dependency Injection, Inversion of Control

## Further Reading

- **Clean Code** by Robert C. Martin
- **Clean Architecture** by Robert C. Martin
- **Design Patterns** by Gang of Four
- **Refactoring** by Martin Fowler

## Summary

**SOLID principles create code that is:**
- **Flexible**: Easy to extend with new features
- **Maintainable**: Easy to understand and modify
- **Testable**: Easy to test in isolation
- **Robust**: Changes don't break existing functionality

Start with one principle at a time, practice with the examples, and gradually incorporate them into your daily coding!
