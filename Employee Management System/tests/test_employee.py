import unittest
from unittest.mock import patch
from src.employee_management.employee import Employee, Manager, EmployeeManager

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

class TestManager(unittest.TestCase):
    def test_valid_manager(self):
        manager = Manager(101, "Rahul", 5)
        self.assertEqual(manager.employee_id, 101)
        self.assertEqual(manager.name, "Rahul")
        self.assertEqual(manager.team_size, 5)

    def test_manager_inherits_from_employee(self):
        manager = Manager(101, "Rahul", 5)
        self.assertIsInstance(manager, Employee)

    def test_manager_team_size_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            Manager(101, "Rahul", -1)

    def test_manager_default_team_size(self):
        manager = Manager(101, "Rahul")
        self.assertEqual(manager.team_size, 0)

    def test_manager_string(self):
        manager = Manager(101, "Rahul", 5)
        self.assertEqual(str(manager),"Manager ID: 101, Name: Rahul, Team Size: 5")

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.find_employee_by_id(101),employee)

    def test_add_loaded_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_loaded_employee(employee)
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.find_employee_by_id(101),employee)

    @patch("builtins.print")
    def test_duplicate_employee_id_is_not_added(self, mock_print):
        employee1 = Employee(101, "Rahul")
        employee2 = Employee(101, "Amit")
        self.manager.add_employee(employee1)
        self.manager.add_employee(employee2)
        self.assertEqual(len(self.manager), 1)
        mock_print.assert_called_with("Employee ID already exists.")

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

    @patch("builtins.print")
    def test_remove_missing_employee(self, mock_print):
        self.manager.add_employee(Employee(101, "Rahul"))
        self.manager.remove_employee(999)
        self.assertEqual(len(self.manager), 1)
        mock_print.assert_called_with("Employee not found.")

    def test_update_existing_employee(self):
        employee = Employee(101, "Rahul")
        self.manager.add_employee(employee)
        self.manager.update_employee(101, "Amit")
        updated_employee = self.manager.find_employee_by_id(101)
        self.assertEqual(updated_employee.name, "Amit")

    @patch("builtins.print")
    def test_update_missing_employee(self, mock_print):
        self.manager.add_employee(Employee(101, "Rahul"))
        self.manager.update_employee(999, "Amit")
        mock_print.assert_called_with("Employee not found.")

    def test_search_employee_by_name(self):
        employee1 = Employee(101, "Rahul")
        employee2 = Employee(102, "Amit")
        self.manager.add_employee(employee1)
        self.manager.add_employee(employee2)
        with patch("builtins.print") as mock_print:
            self.manager.search_employees("Rahul")
            mock_print.assert_any_call("ID:", 101)
            mock_print.assert_any_call("Name:", "Rahul")

    @patch("builtins.print")
    def test_search_employee_with_no_match(self, mock_print):
        self.manager.add_employee(Employee(101, "Rahul"))
        self.manager.search_employees("Amit")
        mock_print.assert_called_with("No matching employee found.")

    @patch("builtins.print")
    def test_find_employee_existing(self, mock_print):
        self.manager.add_employee(Employee(101, "Rahul"))
        self.manager.find_employee(101)
        mock_print.assert_any_call("ID:", 101)
        mock_print.assert_any_call("Name:", "Rahul")

    @patch("builtins.print")
    def test_find_employee_missing(self, mock_print):
        self.manager.find_employee(999)
        mock_print.assert_called_with("Employee not found.")

    @patch("builtins.print")
    def test_list_employees(self, mock_print):
        self.manager.add_employee(Employee(101, "Rahul"))
        self.manager.list_employees()
        mock_print.assert_any_call("ID:", 101)
        mock_print.assert_any_call("Name:", "Rahul")

    @patch("builtins.print")
    def test_list_empty_employees(self, mock_print):
        self.manager.list_employees()
        mock_print.assert_called_with("No employees available.")

if __name__ == "__main__":
    unittest.main()