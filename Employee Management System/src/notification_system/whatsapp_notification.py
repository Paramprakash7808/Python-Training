import logging
from .notification import Notification

logger = logging.getLogger("notification_system")

class WhatsAppNotification(Notification):
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def validate(self):
        if not self.phone_number:
            raise ValueError("Phone number is required.")
        if not self.phone_number.isdigit():
            raise ValueError("Phone number must contain only numbers.")
        if not self.message:
            raise ValueError("Message is required.")

    def send(self):
        try:
            self.validate()
            logger.info("WhatsApp notification attempt for %s",self.phone_number)
            print(f"WhatsApp message sent to "f"{self.phone_number}: {self.message}")
            logger.info("WhatsApp notification sent successfully.")
        except Exception as e:
            logger.error("WhatsApp notification failed: %s",e)

            raise