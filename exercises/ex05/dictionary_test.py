"""These are the test for the dictionary."""

__author__ = "730644820"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import bin_len
import pytest


def test_invert_edge() -> None:
    assert invert({}) == {}


def test_basic_invert():
    original = {"a": "1", "b": "2", "t": "3", "c": "4"}
    returns = {"1": "d", "2": "b", "3": "t", 4: "c"}
    assert invert(original) == returns


def test_invert_but_make_it_duplicates():
    input_dictionary = {"a": "apple", "b": "apple", "c": "chameleon"}
    with pytest.raises(KeyError):
        invert(input_dictionary)


def test_count_edge() -> None:
    assert count({}) == {}


def test_counting_it():
    assert count(["unc", "nccu", "uncg", "unc", "nccu"]) == {
        "unc": 2,
        "nccu": 2,
        "uncg": 1,
    }


def test_count_duplicating():
    assert count(["Phillips", "dey", "Phillips", "sitterson", "dey"]) == {
        "Phillips": 2,
        "dey": 2,
        "sitterson": 1,
    }


def test_for_favorite_color():
    assert favorite_color({"bee": "blue", "unish": "red", "nanda": "green"}) == "blue"


def test_tie_of_favorite_colours():
    assert favorite_color({"bee": "blue", "unish": "red", "nanda": "red"}) == "red"


def test_for_empty_favorite_color():
    assert favorite_color({}) is None


def test_empty_bin_length():
    strings = []
    assert bin_len(strings) == {}


def test_basic_bin_len():
    strings = ["unc", "ncssm", "uncc"]
    expected_result = {3: {"unc"}, 5: {"ncssm"}, 4: {"uncc"}}
    assert bin_len(strings) == expected_result


def test_with_duplicates_bin_len():
    strings = ["unc", "uncc", "uncg", "ncu"]
    expected_results = {3: {"unc", "ncu"}, 4: {"uncc", "uncg"}}
    assert bin_len(strings) == expected_results
