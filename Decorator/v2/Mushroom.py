from Topping import Topping
from Pizza import Pizza
class Mushroom(Topping):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza, "Mushroom", 1.50)
