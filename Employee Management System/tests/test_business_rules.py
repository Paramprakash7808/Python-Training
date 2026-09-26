import unittest
from src.employee_management.business_rules import EmployeeBusinessRules
from src.employee_management.employee import Employee

class TestEmployeeBusinessRules(unittest.TestCase):
    def test_unique_employee_id(self):
        employees = [Employee(101, "Rahul")]
        result = EmployeeBusinessRules.validate_unique_employee_id(employees,102)
        self.assertTrue(result)

    def test_duplicate_employee_id(self):
        employees = [Employee(101, "Rahul")]
        result = EmployeeBusinessRules.validate_unique_employee_id(employees,101)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()