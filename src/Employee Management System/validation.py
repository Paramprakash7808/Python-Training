def get_id():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id <= 0:
                print("ID must be greater than 0.")
                continue
            return emp_id

        except ValueError:
            print("Please enter a valid number.")

def get_name(message):
    while True:
        name = input(message).strip()
        if name == "":
            print("Name cannot be empty.")
            continue

        return name