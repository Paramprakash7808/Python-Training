import unittest
from unittest.mock import patch

from src.validation import get_employee_id, get_employee_name


class TestGetEmployeeId(unittest.TestCase):

    def test_valid_employee_id(self):
        with patch("builtins.input", return_value="101"):
            result = get_employee_id()

        self.assertEqual(result, 101)

    def test_zero_employee_id_is_rejected(self):
        with patch(
            "builtins.input",
            side_effect=["0", "101"]
        ):
            result = get_employee_id()

        self.assertEqual(result, 101)

    def test_negative_employee_id_is_rejected(self):
        with patch(
            "builtins.input",
            side_effect=["-5", "101"]
        ):
            result = get_employee_id()

        self.assertEqual(result, 101)

    def test_non_numeric_employee_id_is_rejected(self):
        with patch(
            "builtins.input",
            side_effect=["abc", "101"]
        ):
            result = get_employee_id()

        self.assertEqual(result, 101)


class TestGetEmployeeName(unittest.TestCase):

    def test_valid_employee_name(self):
        with patch(
            "builtins.input",
            return_value="Rahul"
        ):
            result = get_employee_name("Enter Name: ")

        self.assertEqual(result, "Rahul")

    def test_empty_employee_name_is_rejected(self):
        with patch(
            "builtins.input",
            side_effect=["", "Rahul"]
        ):
            result = get_employee_name("Enter Name: ")

        self.assertEqual(result, "Rahul")

    def test_employee_name_spaces_are_removed(self):
        with patch(
            "builtins.input",
            return_value="  Rahul  "
        ):
            result = get_employee_name("Enter Name: ")

        self.assertEqual(result, "Rahul")


if __name__ == "__main__":
    unittest.main()