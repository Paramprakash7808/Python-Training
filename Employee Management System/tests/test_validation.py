import unittest
from unittest.mock import patch
from src.employee_management.validation import EmployeeValidator

class TestEmployeeValidator(unittest.TestCase):
    def setUp(self):
        self.validator = EmployeeValidator()

    @patch("builtins.input", return_value="101")
    def test_get_valid_employee_id(self, mock_input):
        result = self.validator.get_employee_id()
        self.assertEqual(result, 101)

    @patch("builtins.input",side_effect=["abc", "101"])
    def test_get_employee_id_with_invalid_input(self, mock_input):
        result = self.validator.get_employee_id()
        self.assertEqual(result, 101)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input",side_effect=["0", "101"])
    def test_get_employee_id_with_zero(self, mock_input):
        result = self.validator.get_employee_id()
        self.assertEqual(result, 101)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input",side_effect=["-1", "101"])
    def test_get_employee_id_with_negative_number(self, mock_input):
        result = self.validator.get_employee_id()
        self.assertEqual(result, 101)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", return_value="Rahul")
    def test_get_employee_name(self, mock_input):
        result = self.validator.get_employee_name("Enter Employee Name: ")
        self.assertEqual(result, "Rahul")

    @patch("builtins.input",side_effect=["", "Rahul"])
    def test_get_employee_name_with_empty_input(self, mock_input):
        result = self.validator.get_employee_name("Enter Employee Name: ")
        self.assertEqual(result, "Rahul")
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", return_value="  Rahul  ")
    def test_get_employee_name_with_spaces(self, mock_input):
        result = self.validator.get_employee_name("Enter Employee Name: ")
        self.assertEqual(result, "Rahul")

if __name__ == "__main__":
    unittest.main()