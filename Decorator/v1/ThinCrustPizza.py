from Pizza import Pizza
class ThinCrustPizza(Pizza):
    def __init__(self, mushroom=None, olive=None, onion=None):
        self.mushroom = mushroom
        self.olive = olive
        self.onion = onion

    def get_cost(self):
        base_cost = 5.00  # Base cost for Wheat Base Pizza
        return base_cost + super().get_cost()

    def get_name(self):
        return super().get_name + " Wheat based pizza "