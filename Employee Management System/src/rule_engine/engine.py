from rule import Rule

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        if not isinstance(rule, Rule):
            raise TypeError("Only Rule objects can be added.")

        self.rules.append(rule)

    def evaluate(self, data):
        results = []
        for rule in self.rules:
            result = rule.evaluate(data)
            results.append(result)

        return results