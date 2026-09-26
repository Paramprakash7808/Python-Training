from engine import RuleEngine
from rules import SalaryRule, ExperienceRule, LocationRule

def get_employee_data():
    name = input("Enter employee name: ").strip()
    salary = float(input("Enter employee salary: "))
    experience = float(input("Enter employee experience in years: "))
    location = input("Enter employee location: ").strip()
    return {"name": name,"salary": salary,"experience": experience,"location": location}

def get_rule_configuration():
    minimum_salary = float(input("Enter minimum salary requirement: "))
    minimum_experience = float(input("Enter minimum experience requirement: "))
    allowed_location = input("Enter allowed employee location: ").strip()
    return minimum_salary, minimum_experience, allowed_location

def main():
    print("Rule Engine")
    employee = get_employee_data()
    print()
    print("Rule Configuration")
    (minimum_salary,minimum_experience,allowed_location) = get_rule_configuration()
    engine = RuleEngine()
    engine.add_rule(SalaryRule(minimum_salary))
    engine.add_rule(ExperienceRule(minimum_experience))
    engine.add_rule(LocationRule(allowed_location))
    results = engine.evaluate(employee)
    print()
    print("Rule Evaluation Results")
    for result in results:
        print(f"Rule: {result['rule']}")
        print(f"Passed: {result['passed']}")
        print(f"Message: {result['message']}")
        print()

if __name__ == "__main__":
    main()