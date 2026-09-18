import logging
from .validation import get_employee_id, get_employee_name

logger = logging.getLogger("employee_management")

employees = []

def is_valid_employee(employee):
    if not isinstance(employee, dict):
        return False
    if "id" not in employee or "name" not in employee:
        return False
    if not isinstance(employee["id"], int):
        return False
    if employee["id"] <= 0:
        return False
    if not isinstance(employee["name"], str):
        return False
    if employee["name"].strip() == "":
        return False

    return True

def find_employee_by_id(employee_id):
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue
        if employee["id"] == employee_id:
            return employee

    return None

def get_valid_employees():
    valid_employees = []
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue

        valid_employees.append(employee)
    return valid_employees

def add_employee():
    employee_id = get_employee_id()
    employee_name = get_employee_name("Enter Employee Name: ")
    existing_employee = find_employee_by_id(employee_id)
    if existing_employee is not None:
        logger.warning("Employee ID already exists: %s", employee_id)
        print("Employee ID already exists.")
        return

    employee = {"id": employee_id,"name": employee_name}
    employees.append(employee)
    logger.info("Employee added successfully: ID=%s, Name=%s",employee_id,employee_name)
    print("Employee added successfully.")

def remove_employee():
    employee_id = get_employee_id()
    employee = find_employee_by_id(employee_id)
    if employee is None:
        logger.warning("Employee not found for removal: ID=%s",employee_id)
        print("Employee not found.")
        return

    employees.remove(employee)
    logger.info("Employee removed successfully: ID=%s",employee_id)
    print("Employee removed successfully.")

def update_employee():
    employee_id = get_employee_id()
    employee = find_employee_by_id(employee_id)

    if employee is None:
        logger.warning("Employee not found for update: ID=%s",employee_id)
        print("Employee not found.")
        return

    new_name = get_employee_name("Enter New Employee Name: ")
    old_name = employee["name"]
    employee["name"] = new_name
    logger.info("Employee updated: ID=%s, Name changed from '%s' to '%s'",employee_id,old_name,new_name)
    print("Employee updated successfully.")

def find_employee():
    employee_id = get_employee_id()
    employee = find_employee_by_id(employee_id)
    if employee is None:
        logger.warning("Employee not found: ID=%s",employee_id)
        print("Employee not found.")
        return

    logger.info("Employee found: ID=%s",employee_id)
    print("\nEmployee Found!")
    print("ID:", employee["id"])
    print("Name:", employee["name"])

def list_employees():
    valid_employees = get_valid_employees()
    if len(valid_employees) == 0:
        logger.info("Employee list requested, but no employees are available.")
        print("No employees available.")
        return

    logger.info("Employee list requested. Total employees: %s",len(valid_employees))
    print("\nEmployee List")
    for employee in valid_employees:
        print("ID:", employee["id"])
        print("Name:", employee["name"])

def search_employees():
    search_name = get_employee_name("Enter Employee Name to Search: ")
    logger.info("Employee search started: %s",search_name)

    found = False
    valid_employees = get_valid_employees()
    for employee in valid_employees:
        if search_name.lower() in employee["name"].lower():
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            found = True

    if not found:
        logger.warning("No matching employee found for search: %s",search_name)
        print("No matching employee found.")
    else:
        logger.info("Employee search completed successfully: %s",search_name)