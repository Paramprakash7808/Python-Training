import logging
import os
from .employee import Employee, EmployeeManager
from .validation import EmployeeValidator
from .repository import EmployeeRepository

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "application.log")

def setup_logging():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger("employee_management")

class EmployeeApplication:
    def __init__(self):
        self.validator = EmployeeValidator()
        self.repository = EmployeeRepository()
        self.manager = EmployeeManager()

    def load_data(self):
        employees = self.repository.load_employees()
        for employee in employees:
            self.manager.add_loaded_employee(employee)

    def save_data(self):
        self.repository.save_employees(self.manager.employees)

    def display_menu(self):
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Find Employee")
        print("5. List Employees")
        print("6. Search Employees")
        print("7. Exit")

    def get_menu_choice(self):
        try:
            return int(input("Enter Your Choice: "))
        except ValueError:
            logger.warning("Invalid menu choice entered.")
            print("Please enter a number.")
            return None

    def add_employee(self):
        employee_id = self.validator.get_employee_id()
        employee_name = self.validator.get_employee_name("Enter Employee Name: ")
        employee = Employee(employee_id, employee_name)
        self.manager.add_employee(employee)

    def remove_employee(self):
        employee_id = self.validator.get_employee_id()
        self.manager.remove_employee(employee_id)

    def update_employee(self):
        employee_id = self.validator.get_employee_id()
        new_name = self.validator.get_employee_name("Enter New Employee Name: ")
        self.manager.update_employee(employee_id, new_name)

    def find_employee(self):
        employee_id = self.validator.get_employee_id()
        self.manager.find_employee(employee_id)

    def search_employees(self):
        search_name = self.validator.get_employee_name("Enter Employee Name to Search: ")
        self.manager.search_employees(search_name)

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.add_employee()
            self.save_data()
        elif choice == 2:
            self.remove_employee()
            self.save_data()
        elif choice == 3:
            self.update_employee()
            self.save_data()
        elif choice == 4:
            self.find_employee()
        elif choice == 5:
            self.manager.list_employees()
        elif choice == 6:
            self.search_employees()
        elif choice == 7:
            self.save_data()
            logger.info("Employee Management System exited safely.")
            print("Program exited safely.")
            return False

        else:
            logger.warning("Invalid menu choice: %s",choice)
            print("Invalid choice. Please select 1 to 7.")

        return True

    def run(self):
        self.load_data()
        logger.info("Employee Management System started.")
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            if choice is None:
                continue

            should_continue = self.handle_menu_choice(choice)
            if not should_continue:
                break

def main():
    setup_logging()
    application = EmployeeApplication()

    try:
        application.run()
    except KeyboardInterrupt:
        logger.warning("Program interrupted by user using Ctrl+C.")
        print("\nProgram interrupted by user.")

    except Exception as error:
        logger.exception("Unexpected application error occurred.")
        print("An unexpected application error occurred.")
        print("Error:", error)

if __name__ == "__main__":
    main()