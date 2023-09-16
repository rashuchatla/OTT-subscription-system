from AmazonPrime import AmazonPrime
from HotStar import HotStar
from Netflix import Netflix


class SubscriptionFactory:
    def create_subscription(self, subscription_type,viewing_hours):
        if subscription_type == "Netflix":
            object = Netflix(viewing_hours)
            if object.validate()[0]:
                return object
            else:
                return None
        if subscription_type == "AmazonPrime":
            object = AmazonPrime(viewing_hours)
            if object.validate()[0]:
                return object
            else:
                return None
        if subscription_type == "HotStar":
            object = HotStar(viewing_hours)
            if object.validate()[0]:
                return object
            else:
                return None