import logging
from dataclasses import dataclass

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


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def __len__(self):
        return len(self.employees)

    def __iter__(self):
        return iter(self.employees)

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

        return None

    def add_employee(self, employee):
        existing_employee = self.find_employee_by_id(employee.employee_id)

        if existing_employee is not None:
            logger.warning(
                "Employee ID already exists: %s",
                employee.employee_id
            )
            print("Employee ID already exists.")
            return

        self.employees.append(employee)

        logger.info(
            "Employee added successfully: ID=%s, Name=%s",
            employee.employee_id,
            employee.name
        )
        print("Employee added successfully.")

    def remove_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            logger.warning(
                "Employee not found for removal: ID=%s",
                employee_id
            )
            print("Employee not found.")
            return

        self.employees.remove(employee)

        logger.info(
            "Employee removed successfully: ID=%s",
            employee_id
        )
        print("Employee removed successfully.")

    def update_employee(self, employee_id, new_name):
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            logger.warning(
                "Employee not found for update: ID=%s",
                employee_id
            )
            print("Employee not found.")
            return

        if new_name.strip() == "":
            raise ValueError("Name cannot be empty.")

        old_name = employee.name
        employee.name = new_name.strip()

        logger.info(
            "Employee updated: ID=%s, Name changed from '%s' to '%s'",
            employee_id,
            old_name,
            employee.name
        )
        print("Employee updated successfully.")

    def find_employee(self, employee_id):
        employee = self.find_employee_by_id(employee_id)

        if employee is None:
            logger.warning(
                "Employee not found: ID=%s",
                employee_id
            )
            print("Employee not found.")
            return

        logger.info("Employee found: ID=%s", employee_id)

        print("\nEmployee Found!")
        print("ID:", employee.employee_id)
        print("Name:", employee.name)

    def list_employees(self):
        if len(self.employees) == 0:
            logger.info(
                "Employee list requested, but no employees are available."
            )
            print("No employees available.")
            return

        logger.info(
            "Employee list requested. Total employees: %s",
            len(self.employees)
        )

        print("\nEmployee List")

        for employee in self.employees:
            print("ID:", employee.employee_id)
            print("Name:", employee.name)

    def search_employees(self, search_name):
        logger.info("Employee search started: %s", search_name)

        found = False

        for employee in self.employees:
            if search_name.lower() in employee.name.lower():
                print("ID:", employee.employee_id)
                print("Name:", employee.name)
                found = True

        if not found:
            logger.warning(
                "No matching employee found for search: %s",
                search_name
            )
            print("No matching employee found.")
        else:
            logger.info(
                "Employee search completed successfully: %s",
                search_name
            )