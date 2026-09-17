import json
import logging
import os

from employee import (employees,add_employee,remove_employee,update_employee,find_employee,list_employees,search_employees)

DATA_FILE = "employees.json"
LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "application.log")

# Create logs folder if it does not exist
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# Configure logging
logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger("employee_management")

def load_data():
    if not os.path.exists(DATA_FILE):
        logger.info("No saved employee data found.")
        print("No saved data found. Starting with empty employee list.")
        return
    try:
        # Open and read JSON file
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        # JSON data must be a list
        if not isinstance(data, list):
            logger.error("Invalid data format. JSON data is not a list.")
            print("Invalid data format. Starting with empty employee list.")
            return
        # Check every employee before loading it
        for employee in data:
            if not isinstance(employee, dict):
                logger.error("Invalid employee data found in JSON file.")
                print("Invalid employee data found.")
                return
            if "id" not in employee or "name" not in employee:
                logger.error("Employee data is missing ID or name.")
                print("Invalid employee data found.")
                return
            if not isinstance(employee["id"], int):
                logger.error("Invalid employee ID found in JSON file.")
                print("Invalid employee ID found.")
                return
            if employee["id"] <= 0:
                logger.error("Employee ID must be greater than 0: %s",employee["id"])
                print("Invalid employee ID found.")
                return
            if not isinstance(employee["name"], str):
                logger.error("Invalid employee name found in JSON file.")
                print("Invalid employee name found.")
                return
            if employee["name"].strip() == "":
                logger.error("Empty employee name found in JSON file.")
                print("Invalid employee name found.")
                return

        # Clear old data and load valid data
        employees.clear()
        employees.extend(data)
        logger.info("Employee data loaded successfully. Total employees: %s",len(employees))
        print("Employee data loaded successfully.")

    except json.JSONDecodeError:
        logger.error("Invalid JSON syntax in employee data file.")
        print("Invalid JSON file. Starting with empty employee list.")
    except OSError as error:
        logger.error("Could not read the data file: %s", error)
        print("Could not read the data file.")

def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            # Convert employee list into JSON
            json.dump(employees, file, indent=4)
        logger.info("Employee data saved successfully. Total employees: %s",len(employees))
        print("Employee data saved successfully.")

    except OSError as error:
        logger.error("Could not save employee data: %s", error)
        print("Could not save employee data.")

load_data()

logger.info("Employee Management System started.")

try:
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Find Employee")
        print("5. List Employees")
        print("6. Search Employees")
        print("7. Exit")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            logger.warning("Invalid menu choice entered.")
            print("Please enter a number.")
            continue
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
            break
        else:
            logger.warning("Invalid menu choice: %s", choice)
            print("Invalid choice. Please select 1 to 7.")

except KeyboardInterrupt:
    logger.warning("Program interrupted by user using Ctrl+C.")
    print("\nProgram interrupted by user.")

except Exception as error:
    logger.exception("Unexpected application error occurred.")
    print("An unexpected application error occurred.")
    print("Error:", error)