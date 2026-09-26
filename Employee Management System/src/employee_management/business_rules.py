class EmployeeBusinessRules:
    @staticmethod
    def validate_unique_employee_id(employees, employee_id):
        for employee in employees:
            if employee.employee_id == employee_id:
                print("Employee ID already exists.")
                return False

        return True