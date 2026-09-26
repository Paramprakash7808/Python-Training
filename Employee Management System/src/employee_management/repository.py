import json
import logging
import os
from .employee import Employee

logger = logging.getLogger("employee_management")

class EmployeeRepository:
    def __init__(self, data_file="employees.json"):
        self.data_file = data_file

    def load_employees(self):
        if not os.path.exists(self.data_file):
            logger.info("No saved employee data found.")
            print("No saved data found. Starting with empty employee list.")
            return []

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)

            if not isinstance(data, list):
                logger.error("Invalid data format. JSON data is not a list.")
                print("Invalid data format. Starting with empty employee list.")
                return []

            employees = []

            for employee in data:
                if not isinstance(employee, dict):
                    logger.error("Invalid employee data found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                if "id" not in employee or "name" not in employee:
                    logger.error("Invalid employee data found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                if not isinstance(employee["id"], int):
                    logger.error("Invalid employee ID found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                if employee["id"] <= 0:
                    logger.error("Invalid employee ID found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                if not isinstance(employee["name"], str):
                    logger.error("Invalid employee name found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                if employee["name"].strip() == "":
                    logger.error("Invalid employee name found in JSON file: %s",employee)
                    print("Invalid employee data found.")
                    return []

                employee_object = Employee(employee["id"],employee["name"])
                employees.append(employee_object)

            logger.info("Employee data loaded successfully. Total employees: %s",len(employees))
            print("Employee data loaded successfully.")
            return employees

        except json.JSONDecodeError:
            logger.error("Invalid JSON syntax in employee data file.")
            print("Invalid JSON file. Starting with empty employee list.")
            return []

        except OSError as error:
            logger.error("Could not read the data file: %s",error)
            print("Could not read the data file.")
            return []

    def save_employees(self, employees):
        employee_data = []
        for employee in employees:
            employee_data.append({"id": employee.employee_id,"name": employee.name})

        try:
            with open(self.data_file, "w") as file:
                json.dump(employee_data, file, indent=4)

            logger.info("Employee data saved successfully. Total employees: %s",len(employees))
            print("Employee data saved successfully.")

        except OSError as error:
            logger.error("Could not save the data file: %s",error)
            print("Could not save employee data.")