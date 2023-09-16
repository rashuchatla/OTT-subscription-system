from abc import ABC, abstractmethod


class Subscription(ABC):
    def __init__(self, subscripton_name, viewing_hours):
        self.subscripton_name = subscripton_name
        self.viewing_hours = viewing_hours

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def validate(self):
        pass