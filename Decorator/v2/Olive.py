from Topping import Topping
from Pizza import Pizza

class Olive(Topping):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Olive", 1)
