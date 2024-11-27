"""An example of importing from another module."""

from exercises.imports.helpers import pad_list, add_list
from random import randint


def main() -> None:
    xs: list[int] = [randint(1, 100), 210]
    ys: list[int] = pad_list(xs, 5, 0)
    print(add_list(xs, ys))


if __name__ == "__main__":
    main()
