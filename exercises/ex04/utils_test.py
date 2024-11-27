"""we are testing our utils."""

__author__: str = "730644820"

from exercises.ex04.utils import only_evens
from exercises.ex04.utils import concat, sub


def test_only_edge_case() -> list[int]:
    assert only_evens([1, 3, 5]) == []


def test_concat_add() -> None:
    assert concat([1, 2], [2, 3]) == [1, 2, 2, 3]


def test_sub_two() -> None:
    assert sub([1, 2, 3], 1, 2) == [2]


def test_only_evens_one() -> None:
    assert only_evens([1, 2, 3]) == [2]


# following two are the edge case test :)
def test_concat_edge() -> None:
    assert concat([], []) == []


def test_sub_edge() -> None:
    assert sub([], 10, 20) == []


def test_negative_only_evens() -> None:
    assert only_evens([2, -4, -8]) == [2, -4, -8]


def test_concat_one() -> None:
    assert concat([1], [2]) == [1, 2]


def test_more_sub() -> None:
    assert sub([1, 2, 3, 4, 5], 2, 4) == [3, 4]
