"""Tests for our helper functions."""

from exercises.imports.helpers import pad_list, add_list


def test_pad_list_empty():
    xs: list[int] = []
    actual: list[int] = pad_list(xs, 3, 0)
    expected: list[int] = [0, 0, 0]
    assert actual == expected


def test_pad_list_nonempty():
    xs: list[int] = [1]
    actual: list[int] = pad_list(xs, 3, 0)
    expected: list[int] = [1, 0, 0]
    assert actual == expected


def test_pad_list_nonzero_padding():
    xs: list[int] = [1]
    actual: list[int] = pad_list(xs, 3, -1)
    expected: list[int] = [1, -1, -1]
    assert actual == expected


def test_add_list_single_elemet():
    assert add_list([1], [1]) == [2]
    assert add_list([1], [2]) == [3]


def test_add_list_many_elements():
    assert add_list([1, 2], [3, 4]) == [4, 6]


def test_add_list_empty():
    assert add_list([], []) == []


def test_add_list_unequal_lengths_xs_longer():
    assert add_list([1, 2], [1]) == [2, 2]


def test_add_list_unequal_length_ys_longer():
    assert add_list([1], [1, 2]) == [2, 2]


def test_add_list_gradescope():
    assert add_list([100, 10], [10, 100]) == [110, 110]
