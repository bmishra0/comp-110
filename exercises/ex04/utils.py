"""we are testing I fear."""

__author__: str = "730644820"


def only_evens(even: list[int]) -> list[int]:
    """this returns only even from the input list."""
    index: int = 0
    new: list[int] = []
    while index < len(even):
        if even[index] % 2 == 0:
            new.append(even[index])
        index = index + 1
    return new


def concat(the_list: list[int], other_list: list[int]) -> list[int]:
    """putting together two lists into one."""
    combined_list = the_list + other_list
    return combined_list


def sub(listing: list[int], firstindex: int, sideindex: int) -> list[int]:
    """I think we are trying to pop the index of list."""
    index: int = 0
    subset: list[int] = []
    while index < len(listing):
        if index >= firstindex and index < sideindex:
            subset.append(listing[index])
        index = index + 1
    return subset
