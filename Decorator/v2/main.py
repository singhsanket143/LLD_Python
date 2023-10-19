from BasePizza import WheatBasePizza, ThinCrustPizza
from Mushroom import Mushroom
from Olive import Olive
from Onion import Onion

def main():
    pizza1 = Mushroom(Olive(WheatBasePizza()))
    pizza2 = Onion(ThinCrustPizza())

    print(f"{pizza1.get_description()} costs ${pizza1.get_cost():.2f}")
    print(f"{pizza2.get_description()} costs ${pizza2.get_cost():.2f}")

if __name__ == "__main__":
    main()
