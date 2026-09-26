from rule import Rule

class SalaryRule(Rule):
    def __init__(self, minimum_salary):
        self.minimum_salary = minimum_salary

    def evaluate(self, data):
        salary = data.get("salary", 0)
        if salary >= self.minimum_salary:
            return {"rule": "SalaryRule","passed": True,"message": "Salary requirement passed"}

        return {"rule": "SalaryRule","passed": False,"message": f"Salary must be at least {self.minimum_salary}"}

class ExperienceRule(Rule):
    def __init__(self, minimum_experience):
        self.minimum_experience = minimum_experience

    def evaluate(self, data):
        experience = data.get("experience", 0)
        if experience >= self.minimum_experience:
            return {"rule": "ExperienceRule","passed": True,"message": "Experience requirement passed"}

        return {"rule": "ExperienceRule","passed": False,"message": (f"Experience must be at least "f"{self.minimum_experience} year(s)")}

class LocationRule(Rule):
    def __init__(self, allowed_location):
        self.allowed_location = allowed_location

    def evaluate(self, data):
        location = data.get("location", "").strip()
        if location.lower() == self.allowed_location.lower():
            return {"rule": "LocationRule","passed": True,"message": "Location requirement passed"}

        return {"rule": "LocationRule","passed": False,"message": (f"Employee must be located in "f"{self.allowed_location}")}