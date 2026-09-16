import json
import os

from employee import (employees,add_employee,remove_employee,update_employee,find_employee,list_employees,search_employees)

DATA_FILE = "employees.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        print("No saved data found. Starting with empty employee list.")
        return
    try:
        # Open and read JSON file
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        # JSON data must be a list
        if not isinstance(data, list):
            print("Invalid data format. Starting with empty employee list.")
            return
        # Check every employee before loading it
        for employee in data:
            if not isinstance(employee, dict):
                print("Invalid employee data found.")
                return
            if "id" not in employee or "name" not in employee:
                print("Invalid employee data found.")
                return
            if not isinstance(employee["id"], int):
                print("Invalid employee ID found.")
                return
            if employee["id"] <= 0:
                print("Invalid employee ID found.")
                return
            if not isinstance(employee["name"], str):
                print("Invalid employee name found.")
                return
            if employee["name"].strip() == "":
                print("Invalid employee name found.")
                return
        # Clear old data and load valid data
        employees.clear()
        employees.extend(data)
        print("Employee data loaded successfully.")
    except json.JSONDecodeError:
        # Handles invalid JSON syntax
        print("Invalid JSON file. Starting with empty employee list.")
    except OSError:
        # Handles file reading problems
        print("Could not read the data file.")

def save_data():
    try:
        with open(DATA_FILE, "w") as file:
            # Convert employee list into JSON
            json.dump(employees, file, indent=4)
        print("Employee data saved successfully.")

    except OSError:
        # Handles file writing problems
        print("Could not save employee data.")

load_data()

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
            # User entered something that cannot be converted to integer
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
            print("Program exited safely.")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")

except KeyboardInterrupt:
    # Handles Ctrl+C safely
    print("\nProgram interrupted by user.")

except Exception as error:
    # Handles an unexpected application error
    print("An unexpected application error occurred.")
    print("Error:", error)