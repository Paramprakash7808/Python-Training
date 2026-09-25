import logging
from notification import Notification

logger = logging.getLogger("notification_system")

class EmailNotification(Notification):
    def __init__(self, email, message):
        self.email = email
        self.message = message

    def validate(self):
        if not self.email:
            raise ValueError("Email is required.")
        if "@" not in self.email:
            raise ValueError("Invalid email address.")
        if not self.message:
            raise ValueError("Message is required.")

    def send(self):
        try:
            self.validate()
            logger.info("Email notification attempt for %s",self.email)
            print(f"Email sent to {self.email}: {self.message}")
            logger.info("Email notification sent successfully.")
        except Exception as e:
            logger.error("Email notification failed: %s",e)

            raise