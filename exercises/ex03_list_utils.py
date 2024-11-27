"""This is the testing for Utils"""

__author__: str = "730644820"


def all(one: list[int], numbers: int) -> bool:
    if len(one) == 0:
        return False
    index = 0
    while len(one) > 0:
        if one.pop(0) != numbers:
            return False
        index = index + 1
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest = input.pop(0)

    while len(input) > 0:
        current = input.pop(0)

        if current > largest:
            largest = current

    return largest


def is_equal(input_one: list[int], input_two: list[int]) -> bool:
    if len(input_one) != len(input_two):
        return False

    index = 0
    while index < len(input_one):
        if input_one[index] != input_two[index]:
            return False

        index = index + 1

    return True
