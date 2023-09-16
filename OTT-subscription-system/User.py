
from SubscriptionFactory import SubscriptionFactory


class User:
    def __init__(self, user_name, subscription_data):
        self.subscription_objects = None
        self.total_bill = None
        self.user_name = user_name
        self.subscription_data = subscription_data
        self.SubscriptionFactory = SubscriptionFactory()

    def get_subscription(self):
        self.subscription_objects = []
        for subscription_name, viewing_hours in self.subscription_data.items():
            self.subscription_objects.append(self.SubscriptionFactory.create_subscription(subscription_name,viewing_hours))
        return self.calculate_total_bill()

    def calculate_total_bill(self):
        self.total_bill = 0
        for item in self.subscription_objects:
            if item:
                self.total_bill += item.calculate_bill()
            else:
                return "Invalid units found"
        return self.total_bill
