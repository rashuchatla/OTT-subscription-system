from Subscription import Subscription


class Netflix(Subscription):
    def __init__(self, viewing_hours):
        self.unit_in_hours = 10
        self.price_per_unit = 10
        self.viewing_hours = viewing_hours
        Subscription.__init__(self,"Netflix",viewing_hours)

    def calculate_bill(self):
        return (self.viewing_hours // self.unit_in_hours) * self.price_per_unit

    def validate(self):
        if self.viewing_hours % self.unit_in_hours != 0:
            return False,"Netflix allows vieiwng hours in multiples of {} only".format(self.unit_in_hours)
        return True,"OK"