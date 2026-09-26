import json
import logging
import os
from .employee import Employee
from .repository import EmployeeRepositoryInterface

logger = logging.getLogger("employee_management")

class JsonEmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, data_file="employees.json"):
        self.data_file = data_file

    def load_employees(self):
        if not os.path.exists(self.data_file):
            logger.info("No JSON employee data found.")
            print("No saved data found. Starting with empty employee list.")
            return []

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)

            employees = []
            for item in data:
                employee = Employee(item["id"], item["name"])
                employees.append(employee)

            logger.info("Employee data loaded from JSON. Total employees: %s", len(employees))
            print("Employee data loaded successfully.")
            return employees

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            logger.error("Could not read JSON employee data: %s", error)
            print("Could not read employee data.")
            return []

    def save_employees(self, employees):
        data = []
        for employee in employees:
            data.append({"id": employee.employee_id,"name": employee.name})

        try:
            with open(self.data_file, "w") as file:
                json.dump(data, file, indent=4)

            logger.info("Employee data saved to JSON. Total employees: %s", len(employees))
            print("Employee data saved successfully.")

        except OSError as error:
            logger.error("Could not save JSON employee data: %s", error)
            print("Could not save employee data.")