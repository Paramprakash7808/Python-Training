import json
import logging
import os
from .employee import (employees,add_employee,remove_employee,update_employee,find_employee,list_employees,search_employees,is_valid_employee,)

DATA_FILE = "employees.json"
LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "application.log")

def setup_logging():
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger("employee_management")

def load_data():
    if not os.path.exists(DATA_FILE):
        logger.info("No saved employee data found.")
        print("No saved data found. Starting with empty employee list.")
        return

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            logger.error("Invalid data format. JSON data is not a list.")
            print("Invalid data format. Starting with empty employee list.")
            return

        for employee in data:
            if not is_valid_employee(employee):
                logger.error("Invalid employee data found in JSON file: %s",employee)
                print("Invalid employee data found.")
                return

        employees.clear()
        employees.extend(data)
        logger.info("Employee data loaded successfully. Total employees: %s",len(employees))
        print("Employee data loaded successfully.")

    except json.JSONDecodeError:
        logger.error("Invalid JSON syntax in employee data file.")
        print("Invalid JSON file. Starting with empty employee list.")
    except OSError as error:
        logger.error("Could not read the data file: %s",error)
        print("Could not read the data file.")

def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(employees, file, indent=4)

        logger.info("Employee data saved successfully. Total employees: %s",len(employees))
        print("Employee data saved successfully.")
    except OSError as error:
        logger.error("Could not save the data file: %s",error)
        print("Could not save employee data.")

def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Find Employee")
    print("5. List Employees")
    print("6. Search Employees")
    print("7. Exit")

def get_menu_choice():
    try:
        return int(input("Enter Your Choice: "))
    except ValueError:
        logger.warning("Invalid menu choice entered.")
        print("Please enter a number.")
        return None

def handle_menu_choice(choice):
    if choice == 1:
        add_employee()
        save_data()
    elif choice == 2:
        remove_employee()
        save_data()
    elif choice == 3:
        update_employee()
        save_data()
    elif choice == 4:
        find_employee()
    elif choice == 5:
        list_employees()
    elif choice == 6:
        search_employees()
    elif choice == 7:
        save_data()
        logger.info("Employee Management System exited safely.")
        print("Program exited safely.")
        return False
    else:
        logger.warning("Invalid menu choice: %s",choice)
        print("Invalid choice. Please select 1 to 7.")

    return True

def run_application():
    load_data()
    logger.info("Employee Management System started.")
    while True:
        display_menu()
        choice = get_menu_choice()
        if choice is None:
            continue

        should_continue = handle_menu_choice(choice)
        if not should_continue:
            break

def main():
    setup_logging()
    try:
        run_application()
    except KeyboardInterrupt:
        logger.warning("Program interrupted by user using Ctrl+C.")
        print("\nProgram interrupted by user.")
    except Exception as error:
        logger.exception("Unexpected application error occurred.")
        print("An unexpected application error occurred.")
        print("Error:", error)

if __name__ == "__main__":
    main()