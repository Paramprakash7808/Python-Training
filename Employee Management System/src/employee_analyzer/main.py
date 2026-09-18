import json

from analyzer import (
    get_department_analysis,
    get_highest_salary,
    get_lowest_salary,
    get_average_salary,
    filter_by_department,
    filter_by_location,
    filter_by_experience,
    analyze_experience,
    sort_employees,
    search_employees,
)

from validation import (
    find_duplicate_employees,
    separate_valid_and_invalid_employees,
)


DATA_FILE = "employees.json"


def load_employees():
    try:
        with open(DATA_FILE, "r") as file:
            employees = json.load(file)

        if not isinstance(employees, list):
            print("Employee data must be a list.")
            return []

        return employees

    except FileNotFoundError:
        print(f"{DATA_FILE} file not found.")
        return []

    except json.JSONDecodeError:
        print(f"{DATA_FILE} contains invalid JSON.")
        return []


def save_employees(employees):
    with open(DATA_FILE, "w") as file:
        json.dump(employees, file, indent=4)

    print("Employee data saved successfully.")


def get_employee_input():
    print("\nEnter Employee Details")
    print("----------------------")

    employee_id = input("Enter employee ID: ").strip()
    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()
    salary = input("Enter salary: ").strip()
    experience = input("Enter experience in years: ").strip()
    location = input("Enter location: ").strip()

    try:
        salary = float(salary)
    except ValueError:
        print("Salary must be a number.")
        return None

    try:
        experience = float(experience)
    except ValueError:
        print("Experience must be a number.")
        return None

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary,
        "experience": experience,
        "location": location,
    }

    return employee


def add_employee(employees):
    employee = get_employee_input()

    if employee is None:
        return

    employees.append(employee)
    save_employees(employees)

    print("Employee added successfully.")


def display_employee(employee):
    print(
        f"{employee['id']} | "
        f"{employee['name']} | "
        f"{employee['department']} | "
        f"{employee['salary']} | "
        f"{employee['experience']} years | "
        f"{employee['location']}"
    )


def show_department_analysis(valid_employees):
    analysis = get_department_analysis(valid_employees)

    print("\nDepartment Analysis")

    if not analysis:
        print("No valid employee records available.")
        return

    for department, count in analysis.items():
        print(f"{department}: {count} employee(s)")


def show_salary_analysis(valid_employees):
    highest = get_highest_salary(valid_employees)
    lowest = get_lowest_salary(valid_employees)
    average = get_average_salary(valid_employees)

    print("\nSalary Analysis")

    if highest is None:
        print("No valid employee records available.")
        return

    print(f"Highest Salary: {highest['name']} - {highest['salary']}")
    print(f"Lowest Salary: {lowest['name']} - {lowest['salary']}")
    print(f"Average Salary: {average:.2f}")


def show_experience_analysis(valid_employees):
    analysis = analyze_experience(valid_employees)

    print("\nExperience Analysis")

    if analysis["highest"] is None:
        print("No valid employee records available.")
        return

    print(f"Average Experience: {analysis['average']:.2f} years")

    print(
        f"Highest Experience: "
        f"{analysis['highest']['name']} - "
        f"{analysis['highest']['experience']} years"
    )

    print(
        f"Lowest Experience: "
        f"{analysis['lowest']['name']} - "
        f"{analysis['lowest']['experience']} years"
    )


def show_duplicates(all_employees):
    duplicate_ids = find_duplicate_employees(all_employees)

    print("\nDuplicate Employees")

    if not duplicate_ids:
        print("No duplicate employees found.")
        return

    for employee_id in duplicate_ids:
        print(f"Duplicate Employee ID: {employee_id}")


def show_invalid_records(all_employees):
    _, invalid_employees = separate_valid_and_invalid_employees(
        all_employees
    )

    print("\nInvalid Records")

    if not invalid_employees:
        print("No invalid records found.")
        return

    for record in invalid_employees:
        employee = record["employee"]

        print(f"\nEmployee ID: {employee.get('id', 'Missing')}")
        print("Problems:")

        for error in record["errors"]:
            print(f"- {error}")


def show_filtered_employees(all_employees):
    print("\nFilter Employees")
    print("1. By Department")
    print("2. By Location")
    print("3. By Minimum Experience")

    choice = input("Enter your choice: ").strip()

    valid_employees, _ = separate_valid_and_invalid_employees(
        all_employees
    )

    if choice == "1":
        department = input("Enter department: ").strip()

        results = filter_by_department(
            valid_employees,
            department
        )

    elif choice == "2":
        location = input("Enter location: ").strip()

        results = filter_by_location(
            valid_employees,
            location
        )

    elif choice == "3":
        experience = input("Enter minimum experience: ").strip()

        try:
            minimum_experience = float(experience)

            results = filter_by_experience(
                valid_employees,
                minimum_experience
            )

        except ValueError:
            print("Experience must be a number.")
            return

    else:
        print("Invalid choice.")
        return

    display_employee_list(results)


def show_sorted_employees(all_employees):
    valid_employees, _ = separate_valid_and_invalid_employees(
        all_employees
    )

    print("\nSort Employees")
    print("1. By Name")
    print("2. By Salary")
    print("3. By Experience")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        results = sort_employees(
            valid_employees,
            "name"
        )

    elif choice == "2":
        results = sort_employees(
            valid_employees,
            "salary"
        )

    elif choice == "3":
        results = sort_employees(
            valid_employees,
            "experience"
        )

    else:
        print("Invalid choice.")
        return

    display_employee_list(results)


def show_search_results(all_employees):
    valid_employees, _ = separate_valid_and_invalid_employees(
        all_employees
    )

    search_text = input(
        "Enter employee ID or name: "
    ).strip()

    results = search_employees(
        valid_employees,
        search_text
    )

    print("\nSearch Results")

    display_employee_list(results)


def display_employee_list(employee_list):
    if not employee_list:
        print("No employees found.")
        return

    for employee in employee_list:
        display_employee(employee)


def show_menu():
    print("\nEmployee Data Analyzer")
    print("----------------------")
    print("1. Add employee")
    print("2. Department analysis")
    print("3. Salary analysis")
    print("4. Experience analysis")
    print("5. Filter employees")
    print("6. Show duplicates")
    print("7. Show invalid records")
    print("8. Sort employees")
    print("9. Search employees")
    print("10. Show all employees")
    print("0. Exit")


def main():
    employees = load_employees()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee(employees)

        elif choice == "2":
            valid_employees, _ = separate_valid_and_invalid_employees(
                employees
            )
            show_department_analysis(valid_employees)

        elif choice == "3":
            valid_employees, _ = separate_valid_and_invalid_employees(
                employees
            )
            show_salary_analysis(valid_employees)

        elif choice == "4":
            valid_employees, _ = separate_valid_and_invalid_employees(
                employees
            )
            show_experience_analysis(valid_employees)

        elif choice == "5":
            show_filtered_employees(employees)

        elif choice == "6":
            show_duplicates(employees)

        elif choice == "7":
            show_invalid_records(employees)

        elif choice == "8":
            show_sorted_employees(employees)

        elif choice == "9":
            show_search_results(employees)

        elif choice == "10":
            print("\nAll Employees")
            display_employee_list(employees)

        elif choice == "0":
            print("Exiting Employee Data Analyzer.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()