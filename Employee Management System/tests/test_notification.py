import unittest
from unittest.mock import patch
from src.employee_management.notification import ConsoleNotification

class TestConsoleNotification(unittest.TestCase):
    @patch("builtins.print")
    def test_send_notification(self, mock_print):
        notification = ConsoleNotification()
        notification.send("Employee added successfully.")
        mock_print.assert_called_once_with("Notification:", "Employee added successfully.")

if __name__ == "__main__":
    unittest.main()