import logging
from dataclasses import dataclass
from .business_rules import EmployeeBusinessRules

logger = logging.getLogger("employee_management")

@dataclass
class Employee:
    employee_id: int
    name: str
    def __post_init__(self):
        if self.employee_id <= 0:
            raise ValueError("Employee ID must be greater than 0.")
        if self.name.strip() == "":
            raise ValueError("Name cannot be empty.")

        self.name = self.name.strip()

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"

    def __repr__(self):
        return f"Employee(employee_id={self.employee_id}, name='{self.name}')"

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented

        return self.employee_id == other.employee_id

    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented

        return self.employee_id < other.employee_id

class Manager(Employee):
    def __init__(self, employee_id, name, team_size=0):
        super().__init__(employee_id, name)
        if team_size < 0:
            raise ValueError("Team size cannot be negative.")

        self.team_size = team_size

    def __str__(self):
        return (f"Manager ID: {self.employee_id}, "f"Name: {self.name}, "f"Team Size: {self.team_size}")

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def __len__(self):
        return len(self.employees)

    def add_employee(self, employee):
        if not EmployeeBusinessRules.validate_unique_employee_id(self.employees,employee.employee_id):
            return

        self.employees.append(employee)
        logger.info("Employee added: %s", employee)

    def add_loaded_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                logger.info("Employee removed: %s", employee)
                print("Employee removed successfully.")
                return

        logger.warning("Employee not found: %s", employee_id)
        print("Employee not found.")

    def update_employee(self, employee_id, new_name):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.name = new_name.strip()
                logger.info("Employee updated: %s", employee)
                print("Employee updated successfully.")
                return

        logger.warning("Employee not found: %s", employee_id)
        print("Employee not found.")

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

        return None

    def find_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)
        if employee:
            print("ID:", employee.employee_id)
            print("Name:", employee.name)
            return employee

        print("Employee not found.")
        return None

    def list_employees(self):
        if not self.employees:
            print("No employees available.")
            return

        for employee in self.employees:
            print("ID:", employee.employee_id)
            print("Name:", employee.name)

    def search_employees(self, search_name):
        search_name = search_name.strip().lower()
        found_employees = []
        for employee in self.employees:
            if search_name in employee.name.lower():
                found_employees.append(employee)

        if not found_employees:
            print("No matching employee found.")
            return []

        for employee in found_employees:
            print("ID:", employee.employee_id)
            print("Name:", employee.name)

        return found_employees

if __name__ == "__main__":
    pass