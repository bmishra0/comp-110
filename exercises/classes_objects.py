"""Examples of classes and objects."""


class Pizza:
    """Models a pizza Object!"""

    size: str
    toppings: int
    extra_cheese: bool

    def __init__(self):
        self.size = "medium"
        self.toppings = 0
        self.extra_cheese = False

    def price(self) -> float:
        # medium base price: 10.00
        # Large:15
        # per topping price $0.75
        # Extra cheese $1.50
        total: float = 10.0

        if self.size == "large":
            total = 15.0

        total += self.toppings * 0.75
        if self.extra_cheese:
            total += 1.50

        return total


def pretty_print(pizza: Pizza) -> None:

    print(f"Size: {pizza.size}")
    print(f"toppings: {pizza.toppings}")
    print(f"Extra Cheese: {pizza.extra_cheese}")
    print(f"Price: {pizza.price()}")
    print("=========")


a_pizza: Pizza = Pizza()
another_pizza: Pizza = Pizza()
another_pizza.size = "large"
another_pizza.toppings = 3


pretty_print(a_pizza)
pretty_print(another_pizza)

order: list[Pizza] = [a_pizza, another_pizza]
order_total: float = 0.0
for pizza in order:
    order_total += pizza.price()
print(f"Total: {order_total}")


third_pizza: Pizza = Pizza()
third_pizza.size = "medium"
third_pizza.toppings = 2
third_pizza.extra_cheese = False

order.append(third_pizza)
pretty_print(third_pizza)

order_total = sum(pizza.price() for pizza in order)
print(f"Total: $ {order_total}")
