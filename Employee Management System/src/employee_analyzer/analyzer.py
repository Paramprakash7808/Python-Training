def get_department_analysis(employees):
    department_counts = {}

    for employee in employees:
        department = employee["department"]

        if department not in department_counts:
            department_counts[department] = 0

        department_counts[department] += 1

    return department_counts


def get_highest_salary(employees):
    if not employees:
        return None

    highest_employee = employees[0]

    for employee in employees:
        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee

    return highest_employee


def get_lowest_salary(employees):
    if not employees:
        return None

    lowest_employee = employees[0]

    for employee in employees:
        if employee["salary"] < lowest_employee["salary"]:
            lowest_employee = employee

    return lowest_employee


def get_average_salary(employees):
    if not employees:
        return 0

    total_salary = 0

    for employee in employees:
        total_salary += employee["salary"]

    return total_salary / len(employees)


def filter_by_department(employees, department):
    filtered_employees = []

    for employee in employees:
        if employee["department"].lower() == department.lower():
            filtered_employees.append(employee)

    return filtered_employees


def filter_by_location(employees, location):
    filtered_employees = []

    for employee in employees:
        if employee["location"].lower() == location.lower():
            filtered_employees.append(employee)

    return filtered_employees


def filter_by_experience(employees, minimum_experience):
    filtered_employees = []

    for employee in employees:
        if employee["experience"] >= minimum_experience:
            filtered_employees.append(employee)

    return filtered_employees


def analyze_experience(employees):
    if not employees:
        return {
            "average": 0,
            "highest": None,
            "lowest": None
        }

    total_experience = 0
    highest_experience = employees[0]
    lowest_experience = employees[0]

    for employee in employees:
        total_experience += employee["experience"]

        if employee["experience"] > highest_experience["experience"]:
            highest_experience = employee

        if employee["experience"] < lowest_experience["experience"]:
            lowest_experience = employee

    average_experience = total_experience / len(employees)

    return {
        "average": average_experience,
        "highest": highest_experience,
        "lowest": lowest_experience
    }


def sort_employees(employees, field):
    if not employees:
        return []

    if field not in employees[0]:
        return []

    return sorted(employees, key=lambda employee: employee[field])


def search_employees(employees, search_text):
    matching_employees = []

    search_text = search_text.lower()

    for employee in employees:
        if (
            search_text in employee["id"].lower()
            or search_text in employee["name"].lower()
        ):
            matching_employees.append(employee)

    return matching_employees