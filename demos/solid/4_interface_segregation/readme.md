# Interface Segregation Principle (ISP)

## Definition
**No client should be forced to depend on methods it does not use.**

Instead of one large, "fat" interface, create multiple smaller, focused interfaces. Classes should only implement the interfaces they actually need.

## The Problem

"Fat" interfaces create several issues:

1. **Forced implementation**: Classes must implement methods they don't need
2. **Fake implementations**: Empty methods or methods that throw exceptions
3. **Tight coupling**: Changes to unused methods affect all implementers
4. **Unclear contracts**: What does the interface really require?
5. **Rigid design**: Hard to add new types with different capabilities

In the bad example:
- `BadRobotWorker` is forced to implement `eat()` and `sleep()`
- These methods throw exceptions because robots don't eat or sleep
- Any code expecting a `BadWorker` will crash when using robots

## The Solution

**Break large interfaces into smaller, role-based interfaces:**

1. `Workable`: For anything that can work
2. `Eatable`: For things that eat
3. `Sleepable`: For things that sleep

Now classes implement only what they need:
- `HumanWorker`: implements all three
- `RobotWorker`: implements only `Workable`
- `SuperRobot`: implements `Workable` and `Sleepable`

## Benefits

1. **Flexibility**: Classes implement only relevant methods
2. **Clear contracts**: Each interface has a specific purpose
3. **Easy extension**: Add new worker types without breaking existing code
4. **Better composition**: Mix and match capabilities
5. **Reduced coupling**: Changes to one interface don't affect others

## Role Interfaces

This is an example of **role interfaces** (also called **capability interfaces**):
- Each interface represents a single capability
- Classes implement the capabilities they have
- Client code depends on specific capabilities, not everything

## Real-World Example

Think of electronic devices:
- **Bad**: `IDevice` with methods: `makeCall()`, `takePicture()`, `playMusic()`, `browseWeb()`
  - A music player is forced to implement `makeCall()` (doesn't make sense)
- **Good**: Separate interfaces:
  - `IPhone`: `makeCall()`
  - `ICamera`: `takePicture()`
  - `IMusicPlayer`: `playMusic()`
  - `IWebBrowser`: `browseWeb()`
  - A smartphone implements all four
  - A camera implements only `ICamera`

## ISP vs SRP

These principles are related but different:
- **SRP**: A class should have one reason to change (one responsibility)
- **ISP**: An interface should have one reason to exist (one role/capability)

ISP is about interfaces; SRP is about classes.

## When to Apply

Signs you need ISP:
1. Methods throw `NotImplementedError` or return `None`
2. Empty method bodies
3. Comments like "Not applicable for this class"
4. Implementing classes only use a subset of the interface

Ask: "Does this class really need ALL these methods?"

## Python Note

Python uses **duck typing**, so interfaces are often implicit (via abstract base classes or protocols). However, ISP still applies:
- Don't force classes to implement methods they don't need
- Design cohesive, focused base classes
- Use multiple inheritance to combine capabilities

## Run the Demo

```bash
python demo.py
```

Notice how robots can work without being forced to eat or sleep!

## Key Takeaway

**Many small, focused interfaces are better than one large, general-purpose interface.**

Design interfaces around specific client needs, not around everything a class might do. This creates flexible, maintainable code that's easy to extend.
