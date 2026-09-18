import unittest
from src.employee_analyzer.analyzer import (get_department_analysis,get_highest_salary,get_lowest_salary,get_average_salary,filter_by_department,filter_by_location,filter_by_experience,analyze_experience,sort_employees,search_employees,)
from src.employee_analyzer.validation import (validate_employee,find_duplicate_employees,)

class TestEmployeeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.employees = [
            {"id": "E101","name": "Rahul","department": "IT","salary": 50000,"experience": 3,"location": "Rajkot",},
            {"id": "E102","name": "Priya","department": "HR","salary": 45000,"experience": 2,"location": "Ahmedabad",},
            {"id": "E103","name": "Amit","department": "IT","salary": 70000,"experience": 5,"location": "Rajkot",},
        ]

    def test_department_analysis(self):
        result = get_department_analysis(self.employees)
        self.assertEqual(result["IT"], 2)
        self.assertEqual(result["HR"], 1)

    def test_highest_salary(self):
        result = get_highest_salary(self.employees)
        self.assertEqual(result["name"], "Amit")
        self.assertEqual(result["salary"], 70000)

    def test_lowest_salary(self):
        result = get_lowest_salary(self.employees)
        self.assertEqual(result["name"], "Priya")
        self.assertEqual(result["salary"], 45000)

    def test_average_salary(self):
        result = get_average_salary(self.employees)
        self.assertEqual(result, 55000)

    def test_filter_by_department(self):
        result = filter_by_department(self.employees, "IT")
        self.assertEqual(len(result), 2)

    def test_filter_by_location(self):
        result = filter_by_location(self.employees, "Rajkot")
        self.assertEqual(len(result), 2)

    def test_filter_by_experience(self):
        result = filter_by_experience(self.employees, 3)
        self.assertEqual(len(result), 2)

    def test_experience_analysis(self):
        result = analyze_experience(self.employees)
        self.assertEqual(result["average"], 10 / 3)
        self.assertEqual(result["highest"]["name"], "Amit")
        self.assertEqual(result["lowest"]["name"], "Priya")

    def test_sort_by_salary(self):
        result = sort_employees(self.employees, "salary")
        self.assertEqual(result[0]["name"], "Priya")
        self.assertEqual(result[-1]["name"], "Amit")

    def test_search_employee(self):
        result = search_employees(self.employees, "rahul")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "E101")

    def test_duplicate_employee_detection(self):
        employees = self.employees + [self.employees[0]]
        result = find_duplicate_employees(employees)
        self.assertIn("E101", result)

    def test_invalid_salary(self):
        employee = self.employees[0].copy()
        employee["salary"] = -5000
        errors = validate_employee(employee)
        self.assertIn("Salary must be greater than 0", errors)

    def test_invalid_experience(self):
        employee = self.employees[0].copy()
        employee["experience"] = -2
        errors = validate_employee(employee)
        self.assertIn("Experience cannot be negative", errors)

    def test_missing_field(self):
        employee = self.employees[0].copy()
        del employee["name"]
        errors = validate_employee(employee)
        self.assertIn("Missing field: name", errors)

    def test_empty_employee_list(self):
        self.assertIsNone(get_highest_salary([]))
        self.assertIsNone(get_lowest_salary([]))
        self.assertEqual(get_average_salary([]), 0)

if __name__ == "__main__":
    unittest.main()