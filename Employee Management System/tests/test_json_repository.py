import json
import os
import tempfile
import unittest
from src.employee_management.employee import Employee
from src.employee_management.json_repository import JsonEmployeeRepository

class TestJsonEmployeeRepository(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.repository = JsonEmployeeRepository(self.temp_file.name)

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_save_employees(self):
        employees = [Employee(101, "Rahul"),Employee(102, "Amit")]
        self.repository.save_employees(employees)
        with open(self.temp_file.name, "r") as file:
            data = json.load(file)

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], 101)
        self.assertEqual(data[0]["name"], "Rahul")

    def test_load_employees(self):
        data = [{"id": 101, "name": "Rahul"},{"id": 102, "name": "Amit"}]
        with open(self.temp_file.name, "w") as file:
            json.dump(data, file)

        employees = self.repository.load_employees()
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].employee_id, 101)
        self.assertEqual(employees[0].name, "Rahul")

    def test_load_employees_when_file_does_not_exist(self):
        os.remove(self.temp_file.name)
        employees = self.repository.load_employees()
        self.assertEqual(employees, [])

if __name__ == "__main__":
    unittest.main()