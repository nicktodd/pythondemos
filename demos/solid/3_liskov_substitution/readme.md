# Liskov Substitution Principle (LSP)

## Definition
**Objects of a superclass should be replaceable with objects of a subclass without breaking the application.**

If class B is a subtype of class A, you should be able to use B anywhere you use A, and everything should still work correctly. The subclass must honor the contract of the superclass.

## The Problem

The classic "Square is a Rectangle" problem demonstrates LSP violation:

**Mathematical truth**: A square IS-A rectangle (geometrically)
**Programming reality**: A Square class should NOT inherit from Rectangle

Why? Because they have different **behavioral contracts**:
- **Rectangle**: Width and height can be set independently
- **Square**: Width and height must always be equal

When `BadSquare` inherits from `BadRectangle`:
- `set_width()` unexpectedly changes height
- `set_height()` unexpectedly changes width
- Code expecting rectangle behavior breaks

## The Solution

**Don't force inheritance based on "IS-A" relationships alone.** Consider behavioral compatibility:

1. Create an abstract `Shape` base class
2. Make `Rectangle` and `Square` independent implementations
3. They share the `get_area()` contract but maintain their own invariants

Now both classes can be used interchangeably as `Shape` objects without surprises.

## LSP Violations to Watch For

A subclass violates LSP when it:
1. **Strengthens preconditions**: Requires more than the parent
2. **Weakens postconditions**: Guarantees less than the parent
3. **Throws new exceptions**: Not thrown by the parent
4. **Changes expected behavior**: Side effects differ from parent

## Real-World Example

Think of electric vehicles vs. gas vehicles:
- **Bad design**: `ElectricCar` extends `GasCar` with method `refuel()`
  - Calling `refuel()` on an electric car doesn't make sense
  - Violates LSP
- **Good design**: Both implement `Vehicle` interface with `recharge()`
  - Gas cars: fill tank
  - Electric cars: charge battery
  - Each implements appropriately

## Benefits

1. **Predictable behavior**: Subtypes don't surprise you
2. **Safe substitution**: Use derived classes without fear
3. **Correct abstractions**: Inheritance models actual behavior, not just concepts
4. **Fewer bugs**: Unexpected behavior is a common source of bugs

## The Contract Principle

LSP is about **honoring contracts**:
- The superclass defines a contract (behavior expectations)
- Subclasses must fulfill that contract completely
- Don't create subclasses that break parent expectations

## When to Apply

Before creating inheritance:
1. Can the subclass do **everything** the parent can?
2. Does the subclass behave **the same way** as the parent?
3. Can I use the subclass **anywhere** I use the parent?

If any answer is "no," reconsider the inheritance relationship.

## Run the Demo

```bash
python demo.py
```

Watch how `BadSquare` breaks when used where `BadRectangle` is expected, but the good design works perfectly.

## Key Takeaway

**Inheritance is about behavioral compatibility, not just conceptual relationships.**

Just because something "IS-A" something else in the real world doesn't mean it should inherit from it in code. The subclass must be **behaviorally substitutable**.
