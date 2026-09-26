from src.employee_management.employee import Employee
from src.employee_management.repository import EmployeeRepositoryInterface

class FakeEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self):
        self.employees = []

    def load_employees(self):
        return self.employees.copy()

    def save_employees(self, employees):
        self.employees = employees.copy()