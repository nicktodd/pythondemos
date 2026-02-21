# Single Responsibility Principle (SRP)

## Definition
**A class should have only one reason to change.**

Each class should have a single, well-defined responsibility. If a class has more than one responsibility, those responsibilities become coupled, and changes to one responsibility may affect the class's ability to fulfill the others.

## The Problem

When a class has multiple responsibilities:
- **Hard to maintain**: Changes to one responsibility can break another
- **Hard to test**: You need to set up test data for all responsibilities
- **Hard to reuse**: You can't use one responsibility without bringing along the others
- **Violates separation of concerns**: Different aspects of the system are tangled together

## The Solution

Separate each responsibility into its own class:
- **Employee**: Holds employee data (single source of truth)
- **PayrollCalculator**: Handles payment calculations (financial logic)
- **EmployeeRepository**: Manages database operations (persistence)
- **EmployeeReportGenerator**: Creates reports (presentation/reporting)

## Benefits

1. **Easier to understand**: Each class has a clear, focused purpose
2. **Easier to test**: Test each responsibility in isolation
3. **Easier to maintain**: Changes to reporting don't affect payroll calculations
4. **Better reusability**: Use `PayrollCalculator` with different employee sources
5. **Clearer organization**: Related code is grouped together

## Real-World Example

Think of a restaurant:
- **Chef** (prepares food) - shouldn't also handle billing
- **Waiter** (serves customers) - shouldn't also cook
- **Cashier** (processes payments) - shouldn't also clean tables

Each role has a single, clear responsibility. The same principle applies to classes in software.

## When to Apply

Ask yourself: "What is this class's reason to change?"

If you can think of more than one reason (e.g., "business rules change" AND "database schema changes"), you probably need to split the class.

## Run the Demo

```bash
python demo.py
```

You'll see how the bad example mixes concerns, while the good example separates them cleanly.
