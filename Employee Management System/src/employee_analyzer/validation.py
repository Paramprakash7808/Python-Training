VALID_DEPARTMENTS = {"IT","HR","Finance","Marketing","Sales","Operations"}

def validate_employee(employee):
    errors = []
    if not isinstance(employee, dict):
        return ["Employee record must be a dictionary"]

    required_fields = ["id","name","department","salary","experience","location"]

    for field in required_fields:
        if field not in employee:
            errors.append(f"Missing field: {field}")
            continue

        if employee[field] == "":
            errors.append(f"Empty field: {field}")

    if errors:
        return errors

    if not isinstance(employee["salary"], (int, float)):
        errors.append("Salary must be a number")
    elif employee["salary"] <= 0:
        errors.append("Salary must be greater than 0")

    if not isinstance(employee["experience"], (int, float)):
        errors.append("Experience must be a number")
    elif employee["experience"] < 0:
        errors.append("Experience cannot be negative")

    if employee["department"] not in VALID_DEPARTMENTS:
        errors.append("Unexpected department")

    return errors


def find_duplicate_employees(employees):
    seen_ids = set()
    duplicate_ids = set()
    for employee in employees:
        if not isinstance(employee, dict):
            continue

        employee_id = employee.get("id")
        if not employee_id:
            continue

        if employee_id in seen_ids:
            duplicate_ids.add(employee_id)
        else:
            seen_ids.add(employee_id)

    return list(duplicate_ids)


def separate_valid_and_invalid_employees(employees):
    valid_employees = []
    invalid_employees = []
    for employee in employees:
        errors = validate_employee(employee)
        if errors:
            invalid_employees.append({"employee": employee,"errors": errors})
        else:
            valid_employees.append(employee)

    return valid_employees, invalid_employees