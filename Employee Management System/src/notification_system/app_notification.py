import logging
from notification import Notification

logger = logging.getLogger("notification_system")

class AppNotification(Notification):
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message

    def validate(self):
        if not self.user_id:
            raise ValueError("User ID is required.")
        if not self.message:
            raise ValueError("Message is required.")

    def send(self):
        try:
            self.validate()
            logger.info("App notification attempt for user %s",self.user_id)
            print(f"App notification sent to user " f"{self.user_id}: {self.message}")
            logger.info("App notification sent successfully.")
        except Exception as e:
            logger.error("App notification failed: %s",e)

            raise