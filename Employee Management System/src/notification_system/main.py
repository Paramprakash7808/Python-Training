import logging
from email_notification import EmailNotification
from sms_notification import SMSNotification
from app_notification import AppNotification
from notification_service import NotificationService

logging.basicConfig(filename="logs/notification.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    service = NotificationService()
    email = EmailNotification("prakash@gmail.com","Your order has been shipped.")
    sms = SMSNotification("9876543210","Your OTP is 1234.")
    app = AppNotification(101,"You have a new notification.")
    service.send_notification(email)
    service.send_notification(sms)
    service.send_notification(app)

if __name__ == "__main__":
    main()