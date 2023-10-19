from abc import ABC, abstractmethod

class Pizza(ABC):
    mushroom = None
    olive = None
    onion = None

    @abstractmethod
    def get_cost(self) -> float:
        total_cost = 0.0

        # Assuming some default costs for each ingredient
        if self.mushroom:
            total_cost += 1.50
        if self.olive:
            total_cost += 1.00
        if self.onion:
            total_cost += 0.75

        return total_cost

    @abstractmethod
    def get_name(self) -> str:
        name = ""
        if self.mushroom:
            name += " Musroom "
        if self.olive:
            name += " Olive "
        if self.onion:
            name += " Onion "

        return name

