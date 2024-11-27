"""The some practice with dictionary."""

__author__ = "730644820"


def invert(d: dict[str, str]) -> dict[str, str]:
    the_inverted_dictionary = {}
    for key, value in d.items():
        if value in the_inverted_dictionary:
            raise KeyError(
                f"Duplicate Value '{value}' found. Keys must be unqiue please."
            )
        the_inverted_dictionary[value] = key
    return the_inverted_dictionary


def count(values: list[str]) -> dict[str, int]:
    result_dictionary = {}
    for thing in values:
        if thing in result_dictionary:
            result_dictionary[thing] += 1
        else:
            result_dictionary[thing] = 1
    return result_dictionary


def favorite_color(the_it_colors: dict[str, str]) -> str:
    if len(the_it_colors) == 0:
        return None
    most_frequent_color = None
    maximum_count = -1
    color_counts = {}
    for color in the_it_colors.values():
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

        if color_counts[color] > maximum_count:
            maximum_count = color_counts[color]
            most_frequent_color = color
    return most_frequent_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    bins = {}
    for string in strings:
        length = len(string)
        if length in bins:
            bins[length].add(string)
        else:
            bins[length] = {string}
    return bins
