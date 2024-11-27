"""Algorithm to find greatest factor of an int."""


def greatest_factor(n: int) -> int:
    """Find the greatest factor of n."""
    d: int = n // 2
    while d > 1:
        # print(f"d: {d}")
        if n % d == 0:
            return d
        d = d - 1

    return d


print(greatest_factor(n=151511))
