import unittest
from unittest.mock import patch
from src.employee_management.employee import Employee
from src.employee_management.main import EmployeeApplication
from tests.fake_repository import FakeEmployeeRepository

class TestEmployeeApplication(unittest.TestCase):
    def setUp(self):
        self.repository = FakeEmployeeRepository()
        self.application = EmployeeApplication(repository=self.repository)

    def test_load_data_from_repository(self):
        self.repository.employees = [Employee(101, "Rahul")]
        self.application.load_data()
        self.assertEqual(len(self.application.manager), 1)
        loaded_employee = self.application.manager.find_employee_by_id(101)
        self.assertIsNotNone(loaded_employee)
        self.assertEqual(loaded_employee.name, "Rahul")

    def test_save_data(self):
        employee = Employee(101, "Rahul")
        self.application.manager.add_loaded_employee(employee)
        self.application.save_data()
        self.assertEqual(len(self.repository.employees), 1)
        self.assertEqual(self.repository.employees[0],employee)

    @patch("builtins.input", return_value="1")
    def test_valid_menu_choice(self, mock_input):
        result = self.application.get_menu_choice()
        self.assertEqual(result, 1)

    @patch("builtins.input", return_value="7")
    def test_exit_menu_choice(self, mock_input):
        result = self.application.get_menu_choice()
        self.assertEqual(result, 7)

    @patch("builtins.input", return_value="abc")
    def test_invalid_menu_choice(self, mock_input):
        result = self.application.get_menu_choice()
        self.assertIsNone(result)

    @patch.object(EmployeeApplication, "add_employee")
    @patch.object(EmployeeApplication, "save_data")
    def test_add_employee_menu_choice(self,mock_save_data,mock_add_employee):
        result = self.application.handle_menu_choice(1)
        mock_add_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch.object(EmployeeApplication, "remove_employee")
    @patch.object(EmployeeApplication, "save_data")
    def test_remove_employee_menu_choice(self,mock_save_data,mock_remove_employee):
        result = self.application.handle_menu_choice(2)
        mock_remove_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch.object(EmployeeApplication, "update_employee")
    @patch.object(EmployeeApplication, "save_data")
    def test_update_employee_menu_choice(self,mock_save_data,mock_update_employee):
        result = self.application.handle_menu_choice(3)
        mock_update_employee.assert_called_once()
        mock_save_data.assert_called_once()
        self.assertTrue(result)

    @patch.object(EmployeeApplication, "find_employee")
    def test_find_employee_menu_choice(self, mock_find_employee):
        result = self.application.handle_menu_choice(4)
        mock_find_employee.assert_called_once()
        self.assertTrue(result)

    def test_list_employee_menu_choice(self):
        with patch.object(self.application.manager,"list_employees") as mock_list_employees:
            result = self.application.handle_menu_choice(5)
            mock_list_employees.assert_called_once()
            self.assertTrue(result)

    @patch.object(EmployeeApplication, "search_employees")
    def test_search_employee_menu_choice(self,mock_search_employees):
        result = self.application.handle_menu_choice(6)
        mock_search_employees.assert_called_once()
        self.assertTrue(result)

    @patch.object(EmployeeApplication, "save_data")
    def test_exit_menu_choice(self, mock_save_data):
        result = self.application.handle_menu_choice(7)
        mock_save_data.assert_called_once()
        self.assertFalse(result)

    def test_invalid_menu_choice(self):
        result = self.application.handle_menu_choice(99)
        self.assertTrue(result)

    @patch.object(EmployeeApplication, "load_data")
    @patch.object(EmployeeApplication, "display_menu")
    @patch.object(EmployeeApplication, "get_menu_choice", return_value=7)
    @patch.object(EmployeeApplication, "handle_menu_choice", return_value=False)
    def test_application_exits_safely(self,mock_handle_menu_choice,mock_get_menu_choice,mock_display_menu,mock_load_data):
        self.application.run()
        mock_load_data.assert_called_once()
        mock_display_menu.assert_called_once()
        mock_get_menu_choice.assert_called_once()
        mock_handle_menu_choice.assert_called_once_with(7)

if __name__ == "__main__":
    unittest.main()