import logging
from validation import get_id, get_name

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

def add_employee():
    emp_id = get_id()
    emp_name = get_name("Enter Employee Name: ")
    # Check duplicate ID
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            logger.warning("Employee ID already exists: %s", emp_id)
            print("Employee ID already exists.")
            return

    employee = {"id": emp_id,"name": emp_name}
    employees.append(employee)
    logger.info("Employee added successfully: ID=%s, Name=%s",emp_id,emp_name)
    print("Employee added successfully.")

def remove_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            employees.remove(employee)
            logger.info("Employee removed successfully: ID=%s", emp_id)
            print("Employee removed successfully.")
            return

    logger.warning("Employee not found for removal: ID=%s", emp_id)
    print("Employee not found.")

def update_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue

        if employee["id"] == emp_id:
            new_name = get_name("Enter New Employee Name: ")
            old_name = employee["name"]
            employee["name"] = new_name
            logger.info("Employee updated: ID=%s, Name changed from '%s' to '%s'",emp_id,old_name,new_name)
            print("Employee updated successfully.")
            return

    logger.warning("Employee not found for update: ID=%s", emp_id)
    print("Employee not found.")

def find_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue

        if employee["id"] == emp_id:
            logger.info("Employee found: ID=%s", emp_id)
            print("\nEmployee Found!")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            return
    logger.warning("Employee not found: ID=%s", emp_id)
    print("Employee not found.")

def list_employees():
    if len(employees) == 0:
        logger.info("Employee list requested, but no employees are available.")
        print("No employees available.")
        return

    logger.info("Employee list requested. Total employees: %s",len(employees))
    print("\nEmployee List")
    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue
        print("ID:", employee["id"])
        print("Name:", employee["name"])

def search_employees():
    search = get_name("Enter Employee Name to Search: ")
    logger.info("Employee search started: %s", search)
    found = False

    for employee in employees:
        if not is_valid_employee(employee):
            logger.error("Invalid employee data found: %s", employee)
            print("Invalid employee data found.")
            continue
        if search.lower() in employee["name"].lower():
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            found = True

    if found == False:
        logger.warning("No matching employee found for search: %s",search)
        print("No matching employee found.")
    else:
        logger.info("Employee search completed successfully: %s",search)