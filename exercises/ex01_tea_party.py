"""This is a planning for Tea Party"""

__author__: str = "730644820"


def main_planner(guests: int) -> None:
    """This is planning for the tea party!"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=guests * 2, treat_count=guests * 3)))
    return None


def tea_bags(people: int) -> int:
    """This is for the number of people at the party"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats consumeed by people"""
    return 3 * (tea_bags(people=people) // 2)


def cost(tea_count: int, treat_count: int) -> float:
    """This calculates the cost of tea bags and treats combined."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
