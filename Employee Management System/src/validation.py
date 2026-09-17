import logging

logger = logging.getLogger("employee_management")

def get_id():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id <= 0:
                logger.warning("Invalid employee ID entered: %s", emp_id)
                print("ID must be greater than 0.")
                continue
            return emp_id
        except ValueError:
            logger.warning("Invalid employee ID input: non-numeric value entered")
            print("Please enter a valid number.")

def get_name(message):
    while True:
        name = input(message).strip()
        if name == "":
            logger.warning("Invalid employee name input: empty name entered")
            print("Name cannot be empty.")
            continue
        return name