from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def evaluate(self, data):
        pass