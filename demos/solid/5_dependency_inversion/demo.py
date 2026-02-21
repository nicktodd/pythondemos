# Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules
# Both should depend on abstractions

from abc import ABC, abstractmethod

# BAD: High-level code depends directly on low-level implementations
class BadEmailService:
    """Low-level module - concrete implementation"""
    def send_email(self, message, recipient):
        print(f"Sending email to {recipient}: {message}")


class BadSMSService:
    """Low-level module - concrete implementation"""
    def send_sms(self, message, phone):
        print(f"Sending SMS to {phone}: {message}")


class BadNotificationService:
    """High-level module - depends on concrete low-level modules"""
    def __init__(self):
        self.email_service = BadEmailService()  # Direct dependency!
        self.sms_service = BadSMSService()      # Direct dependency!
    
    def notify_by_email(self, message, recipient):
        self.email_service.send_email(message, recipient)
    
    def notify_by_sms(self, message, phone):
        self.sms_service.send_sms(message, phone)
    
    # To add push notifications, we'd need to modify this class!


# GOOD: Both high-level and low-level modules depend on abstractions
class MessageSender(ABC):
    """Abstraction - the contract for sending messages"""
    @abstractmethod
    def send(self, message, recipient):
        pass


# Low-level modules implement the abstraction
class EmailSender(MessageSender):
    """Concrete implementation of email sending"""
    def send(self, message, recipient):
        print(f"Email to {recipient}: {message}")


class SMSSender(MessageSender):
    """Concrete implementation of SMS sending"""
    def send(self, message, recipient):
        print(f"SMS to {recipient}: {message}")


class PushNotificationSender(MessageSender):
    """NEW implementation - no changes needed to high-level code!"""
    def send(self, message, recipient):
        print(f"Push notification to {recipient}: {message}")


class SlackSender(MessageSender):
    """Another new implementation"""
    def send(self, message, recipient):
        print(f"Slack message to {recipient}: {message}")


# High-level module depends on the abstraction
class NotificationService:
    """High-level module - depends on abstraction, not concrete implementations"""
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Depends on abstraction!
    
    def notify(self, message, recipient):
        self.sender.send(message, recipient)


# Even better: Support multiple senders
class MultiChannelNotificationService:
    """Can use any combination of senders"""
    def __init__(self, senders: list[MessageSender]):
        self.senders = senders
    
    def notify_all(self, message, recipient):
        for sender in self.senders:
            sender.send(message, recipient)


# Usage
if __name__ == "__main__":
    print("=== Bad Example - Tight Coupling ===")
    bad_service = BadNotificationService()
    bad_service.notify_by_email("Hello!", "user@example.com")
    bad_service.notify_by_sms("Hello!", "+44 123 456 7890")
    print("Problem: To add push notifications, we must modify BadNotificationService!")
    
    print("\n=== Good Example - Loose Coupling ===")
    
    # Same high-level code works with different implementations
    email_notifier = NotificationService(EmailSender())
    email_notifier.notify("Meeting at 3pm", "alice@example.com")
    
    sms_notifier = NotificationService(SMSSender())
    sms_notifier.notify("Meeting at 3pm", "+44 789 123 4567")
    
    # NEW: Push notifications - no changes to NotificationService!
    push_notifier = NotificationService(PushNotificationSender())
    push_notifier.notify("Meeting at 3pm", "user123")
    
    # NEW: Slack notifications
    slack_notifier = NotificationService(SlackSender())
    slack_notifier.notify("Meeting at 3pm", "@bob")
    
    print("\n=== Multi-Channel Notifications ===")
    multi_service = MultiChannelNotificationService([
        EmailSender(),
        SMSSender(),
        PushNotificationSender(),
        SlackSender()
    ])
    multi_service.notify_all("Server maintenance in 1 hour!", "admin@example.com")
    
    print("\n All new senders added without modifying existing code!")
