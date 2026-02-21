# Dependency Inversion Principle (DIP)

## Definition
**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

Additionally: **Abstractions should not depend on details. Details should depend on abstractions.**

## The Problem

Traditional layered architecture:
```
High-level (Business Logic) 
    ↓ depends on
Low-level (Implementation Details)
```

This creates problems:
1. **Tight coupling**: High-level code tied to specific implementations
2. **Hard to test**: Can't easily mock dependencies
3. **Inflexible**: Changing implementations requires changing high-level code
4. **Rigid**: Adding new implementations requires modifying existing code

In the bad example:
- `BadNotificationService` directly creates `BadEmailService` and `BadSMSService`
- To add push notifications, you must modify `BadNotificationService`
- Can't test without actually sending emails/SMS

## The Solution

**Invert the dependency** using abstraction:

```
High-level (Business Logic) ──┐
                              ├──> Abstraction (Interface)
Low-level (Implementations) ──┘
```

1. Create `MessageSender` abstraction
2. High-level `NotificationService` depends on `MessageSender`
3. Low-level implementations (`EmailSender`, `SMSSender`) implement `MessageSender`
4. Dependencies are **injected** into `NotificationService`

Now both layers depend on the abstraction, not on each other.

## Benefits

1. **Loose coupling**: High-level code independent of implementations
2. **Easy testing**: Inject mock implementations
3. **Flexibility**: Swap implementations at runtime
4. **Open/Closed**: Add new senders without modifying existing code
5. **Reusability**: High-level logic works with any sender

## Dependency Injection

DIP often uses **Dependency Injection (DI)**:

```python
# Dependencies are injected via constructor
service = NotificationService(EmailSender())

# Easy to change
service = NotificationService(SMSSender())

# Easy to test
service = NotificationService(MockSender())
```

Benefits of DI:
- Explicit dependencies (clear what the class needs)
- Flexible configuration
- Testable (inject mocks)
- Single Responsibility (don't create dependencies)

## Real-World Example

Think of a media player:
- **Bad**: `MediaPlayer` directly uses `MP3Decoder`, `WAVDecoder`, `FLACDecoder`
  - Hard-coded dependencies
  - To add AAC support, modify `MediaPlayer`
- **Good**: `MediaPlayer` depends on `IAudioDecoder` interface
  - Each format implements `IAudioDecoder`
  - Inject the decoder: `MediaPlayer(MP3Decoder())`
  - Add AAC: create `AACDecoder` (no changes to `MediaPlayer`)

## DIP vs Dependency Injection

**DIP** is a principle: depend on abstractions
**DI** is a technique: pass dependencies from outside

DI is one way to achieve DIP, but not the only way.

## Traditional vs Inverted

**Traditional dependency:**
```python
class Service:
    def __init__(self):
        self.db = MySQLDatabase()  # Direct dependency
```

**Inverted dependency:**
```python
class Service:
    def __init__(self, db: IDatabase):  # Depends on abstraction
        self.db = db

# Usage:
service = Service(MySQLDatabase())  # Inject concrete implementation
```

The dependency direction is **inverted**:
- Before: High-level → Low-level
- After: Both → Abstraction

## When to Apply

Apply DIP when:
1. High-level code uses low-level implementations directly
2. You want to swap implementations (testing, different environments)
3. You anticipate multiple implementations of the same concept
4. You want to isolate changes to implementation details

## The Hollywood Principle

DIP is related to the **Hollywood Principle**:
> "Don't call us, we'll call you"

Instead of high-level code creating and calling low-level code directly, you inject the low-level code and it gets called through the abstraction.

## Run the Demo

```bash
python demo.py
```

See how easy it is to add new message senders without touching existing code!

## Key Takeaway

**Depend on abstractions, not concretions.**

By inverting dependencies so both high-level and low-level code depend on abstractions, you create flexible, testable, maintainable systems. This is the foundation of modern software architecture (like Clean Architecture, Hexagonal Architecture).

The "inversion" is that instead of high-level code depending on (controlling) low-level code, both depend on abstractions defined by the high-level needs.
