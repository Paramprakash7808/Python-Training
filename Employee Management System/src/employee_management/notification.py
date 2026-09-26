from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    @abstractmethod
    def send(self, message):
        pass

class ConsoleNotification(NotificationInterface):
    def send(self, message):
        print("Notification:", message)