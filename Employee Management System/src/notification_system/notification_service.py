import logging

logger = logging.getLogger("notification_system")

class NotificationService:
    def send_notification(self, notification):
        try:
            logger.info("Sending notification: %s",notification.__class__.__name__)
            notification.send()
            logger.info("Notification completed successfully.")
        except Exception as e:
            logger.error("Notification failed: %s",e)
            print(f"Notification failed: {e}")