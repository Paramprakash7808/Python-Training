import unittest
from src.employee_management.employee import Employee
from tests.fake_repository import FakeEmployeeRepository

class TestFakeEmployeeRepository(unittest.TestCase):
    def setUp(self):
        self.repository = FakeEmployeeRepository()

    def test_save_and_load_employees(self):
        employees = [Employee(101, "Rahul"),Employee(102, "Amit")]
        self.repository.save_employees(employees)
        loaded_employees = self.repository.load_employees()
        self.assertEqual(loaded_employees, employees)

    def test_load_empty_repository(self):
        employees = self.repository.load_employees()
        self.assertEqual(employees, [])

    def test_repository_returns_copy(self):
        employees = [Employee(101, "Rahul")]
        self.repository.save_employees(employees)
        loaded_employees = self.repository.load_employees()
        loaded_employees.clear()
        self.assertEqual(len(self.repository.employees), 1)

if __name__ == "__main__":
    unittest.main()