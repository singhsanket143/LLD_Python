from Pizza import Pizza

class WheatBasePizza(Pizza):
    def __init__(self):
        super().__init__("Wheat Base Pizza", 5.00)

    def get_description(self) -> str:
        return self._description

    def get_cost(self) -> float:
        return self._cost

class ThinCrustPizza(Pizza):
    def __init__(self):
        super().__init__("Thin Crust Pizza", 6.00)

    def get_description(self) -> str:
        return self._description

    def get_cost(self) -> float:
        return self._cost
