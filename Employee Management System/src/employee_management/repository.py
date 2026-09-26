import logging
import sqlite3
from abc import ABC, abstractmethod
from .employee import Employee

logger = logging.getLogger("employee_management")

class EmployeeRepositoryInterface(ABC):
    @abstractmethod
    def load_employees(self):
        pass

    @abstractmethod
    def save_employees(self, employees):
        pass

class EmployeeRepository(EmployeeRepositoryInterface):
    def __init__(self, database="employees.db"):
        self.database = database

    def create_table(self):
        try:
            with sqlite3.connect(self.database) as connection:
                connection.execute("""CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL)""")

            logger.info("Employee database table is ready.")
        except sqlite3.Error as error:
            logger.error("Could not create employee table: %s", error)
            print("Could not create employee database table.")

    def load_employees(self):
        self.create_table()
        try:
            with sqlite3.connect(self.database) as connection:
                cursor = connection.execute("SELECT id, name FROM employees ORDER BY id")
                rows = cursor.fetchall()

            employees = []
            for employee_id, name in rows:
                employee = Employee(employee_id, name)
                employees.append(employee)

            logger.info("Employee data loaded successfully. Total employees: %s", len(employees))
            if employees:
                print("Employee data loaded successfully.")
            else:
                print("No saved data found. Starting with empty employee list.")

            return employees

        except sqlite3.Error as error:
            logger.error("Could not read employee database: %s", error)
            print("Could not read employee data.")
            return []

    def save_employees(self, employees):
        self.create_table()
        try:
            with sqlite3.connect(self.database) as connection:
                connection.execute("DELETE FROM employees")
                for employee in employees:
                    connection.execute("""INSERT INTO employees (id, name) VALUES (?, ?)""", (employee.employee_id, employee.name))

            logger.info("Employee data saved successfully. Total employees: %s", len(employees))
            print("Employee data saved successfully.")

        except sqlite3.Error as error:
            logger.error("Could not save employee data: %s", error)
            print("Could not save employee data.")