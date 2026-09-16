from validation import get_id, get_name

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
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            print("Employee ID already exists.")
            return
    employee = {"id": emp_id,"name": emp_name}
    employees.append(employee)
    print("Employee added successfully.")

def remove_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            employees.remove(employee)
            print("Employee removed successfully.")
            return
    print("Employee not found.")

def update_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            new_name = get_name("Enter New Employee Name: ")
            employee["name"] = new_name
            print("Employee updated successfully.")
            return
    print("Employee not found.")

def find_employee():
    emp_id = get_id()
    for employee in employees:
        if not is_valid_employee(employee):
            print("Invalid employee data found.")
            continue
        if employee["id"] == emp_id:
            print("\nEmployee Found!")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            return
    print("Employee not found.")

def list_employees():
    if len(employees) == 0:
        print("No employees available.")
        return
    print("\nEmployee List")
    for employee in employees:
        if not is_valid_employee(employee):
            print("Invalid employee data found.")
            continue
        print("ID:", employee["id"])
        print("Name:", employee["name"])

def search_employees():
    search = get_name("Enter Employee Name to Search: ")
    found = False
    for employee in employees:
        if not is_valid_employee(employee):
            print("Invalid employee data found.")
            continue
        if search.lower() in employee["name"].lower():
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            found = True
    if found == False:
        print("No matching employee found.")