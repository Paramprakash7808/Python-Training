import unittest
from unittest.mock import patch
from src.employee_management import employee

class TestEmployeeValidation(unittest.TestCase):
    def test_valid_employee(self):
        employee_data = {"id": 101, "name": "Rahul"}
        result = employee.is_valid_employee(employee_data)
        self.assertTrue(result)

    def test_employee_is_not_dictionary(self):
        employee_data = "Rahul"
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_missing_id(self):
        employee_data = {"name": "Rahul"}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_missing_name(self):
        employee_data = {"id": 101}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_id_must_be_integer(self):
        employee_data = {"id": "101", "name": "Rahul"}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_id_must_be_greater_than_zero(self):
        employee_data = {"id": 0, "name": "Rahul"}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_name_must_be_string(self):
        employee_data = {"id": 101, "name": 123}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

    def test_employee_name_cannot_be_empty(self):
        employee_data = {"id": 101, "name": ""}
        result = employee.is_valid_employee(employee_data)
        self.assertFalse(result)

class TestFindEmployee(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    def test_find_existing_employee(self):
        employee.employees.append({"id": 101, "name": "Rahul"})
        result = employee.find_employee_by_id(101)
        self.assertEqual(result["name"], "Rahul")

    def test_find_missing_employee(self):
        employee.employees.append({"id": 101, "name": "Rahul"})
        result = employee.find_employee_by_id(999)
        self.assertIsNone(result)

    def test_find_employee_from_empty_list(self):
        result = employee.find_employee_by_id(101)
        self.assertIsNone(result)

class TestGetValidEmployees(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    def test_get_valid_employees(self):
        employee.employees.extend([{"id": 101, "name": "Rahul"},{"id": 102, "name": "Amit"}])
        result = employee.get_valid_employees()
        self.assertEqual(len(result), 2)

    def test_invalid_employee_is_not_returned(self):
        employee.employees.extend([{"id": 101, "name": "Rahul"},{"id": 0, "name": "Invalid Employee"}])
        result = employee.get_valid_employees()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 101)

    def test_get_valid_employees_from_empty_list(self):
        result = employee.get_valid_employees()
        self.assertEqual(result, [])

class TestAddEmployee(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    @patch("src.employee_management.employee.get_employee_name",return_value="Rahul")
    @patch("src.employee_management.employee.get_employee_id",return_value=101)
    def test_add_employee_with_valid_data(self,mock_get_id,mock_get_name):
        employee.add_employee()
        self.assertEqual(len(employee.employees), 1)
        self.assertEqual(employee.employees[0]["id"], 101)
        self.assertEqual(employee.employees[0]["name"], "Rahul")

    def test_duplicate_employee_id_is_not_added(self):
        employee.employees.append({"id": 101, "name": "Rahul"})
        with patch("src.employee_management.employee.get_employee_id",return_value=101):
            with patch("src.employee_management.employee.get_employee_name",return_value="Amit"):
                employee.add_employee()

        self.assertEqual(len(employee.employees), 1)
        self.assertEqual(employee.employees[0]["name"], "Rahul")

class TestRemoveEmployee(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    @patch("src.employee_management.employee.get_employee_id",return_value=101)
    def test_remove_existing_employee(self, mock_get_id):
        employee.employees.append({"id": 101, "name": "Rahul"})
        employee.remove_employee()
        self.assertEqual(employee.employees, [])

    @patch("src.employee_management.employee.get_employee_id",return_value=999)
    def test_remove_missing_employee(self, mock_get_id):
        employee.employees.append({"id": 101, "name": "Rahul"})
        employee.remove_employee()
        self.assertEqual(len(employee.employees), 1)

class TestUpdateEmployee(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    @patch("src.employee_management.employee.get_employee_name",return_value="Amit")
    @patch("src.employee_management.employee.get_employee_id",return_value=101)
    def test_update_existing_employee(self,mock_get_id,mock_get_name):
        employee.employees.append({"id": 101, "name": "Rahul"})
        employee.update_employee()
        self.assertEqual(employee.employees[0]["name"], "Amit")

    @patch("src.employee_management.employee.get_employee_name",return_value="Amit")
    @patch("src.employee_management.employee.get_employee_id",return_value=999)
    def test_update_missing_employee(self,mock_get_id,mock_get_name):
        employee.employees.append({"id": 101, "name": "Rahul"})
        employee.update_employee()
        self.assertEqual(employee.employees[0]["name"], "Rahul")

class TestSearchEmployees(unittest.TestCase):
    def setUp(self):
        employee.employees.clear()

    def tearDown(self):
        employee.employees.clear()

    @patch("src.employee_management.employee.get_employee_name",return_value="rahul")
    def test_search_employee_by_name(self, mock_get_name):
        employee.employees.append({"id": 101, "name": "Rahul"})
        with patch("builtins.print") as mock_print:
            employee.search_employees()
        mock_print.assert_any_call("ID:", 101)
        mock_print.assert_any_call("Name:", "Rahul")

    @patch("src.employee_management.employee.get_employee_name",return_value="amit")
    def test_search_employee_with_no_match(self, mock_get_name):
        employee.employees.append({"id": 101, "name": "Rahul"})
        with patch("builtins.print") as mock_print:
            employee.search_employees()
        mock_print.assert_any_call("No matching employee found.")

if __name__ == "__main__":
    unittest.main()