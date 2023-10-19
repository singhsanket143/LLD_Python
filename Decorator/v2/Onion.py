from Topping import Topping
from Pizza import Pizza

class Onion(Topping):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Onion", 2)
