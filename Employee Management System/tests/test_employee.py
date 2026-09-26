import unittest
from unittest.mock import patch
from src.employee_management.employee import Employee, EmployeeManager

class TestEmployee(unittest.TestCase):
    def test_valid_employee(self):
        employee = Employee(101, "Rahul")
        self.assertEqual(employee.employee_id, 101)
        self.assertEqual(employee.name, "Rahul")

    def test_employee_id_must_be_greater_than_zero(self):
        with self.assertRaises(ValueError):
            Employee(0, "Rahul")

    def test_employee_name_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            Employee(101, "")

    def test_employee_name_is_stripped(self):
        employee = Employee(101, "  Rahul  ")
        self.assertEqual(employee.name, "Rahul")

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.find_employee_by_id(101), employee)

    def test_duplicate_employee_id_is_not_added(self):
        employee1 = Employee(101, "Rahul")
        employee2 = Employee(101, "Amit")
        self.manager.add_employee(employee1)
        self.manager.add_employee(employee2)
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.find_employee_by_id(101).name,"Rahul")

    def test_find_existing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        result = self.manager.find_employee_by_id(101)
        self.assertEqual(result, employee)

    def test_find_missing_employee(self):
        result = self.manager.find_employee_by_id(999)
        self.assertIsNone(result)

    def test_remove_existing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.manager.remove_employee(101)
        self.assertEqual(len(self.manager), 0)

    def test_remove_missing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.manager.remove_employee(999)
        self.assertEqual(len(self.manager), 1)

    def test_update_existing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.manager.update_employee(101, "Amit")
        result = self.manager.find_employee_by_id(101)
        self.assertEqual(result.name, "Amit")

    def test_update_missing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.manager.update_employee(999, "Amit")
        result = self.manager.find_employee_by_id(101)
        self.assertEqual(result.name, "Rahul")

    def test_search_employee_by_name(self):
        employee1 = Employee(101, "Rahul")
        employee2 = Employee(102, "Amit")
        self.manager.add_employee(employee1)
        self.manager.add_employee(employee2)
        with patch("builtins.print") as mock_print:
            self.manager.search_employees("rahul")

        mock_print.assert_any_call("ID:", 101)
        mock_print.assert_any_call("Name:", "Rahul")

    def test_search_employee_with_no_match(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        with patch("builtins.print") as mock_print:
            self.manager.search_employees("Amit")

        mock_print.assert_any_call("No matching employee found.")

    def test_add_loaded_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_loaded_employee(employee)
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.find_employee_by_id(101),employee)

if __name__ == "__main__":
    unittest.main()