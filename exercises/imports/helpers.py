"""Some helper functions."""


def pad_list(xs: list[int], to_length: int, padding: int) -> list[int]:
    """Fill xs to ton_len with padding when len(xs) < to_length."""
    copy: list[int] = xs.copy()
    while len(copy) < to_length:
        copy.append(padding)
    return copy


def add_list(xs: list[int], ys: list[int]) -> list[int]:
    """Add the items of two lists together item-by-item."""
    if len(xs) != len(ys):
        if len(xs) > len(ys):
            ys = pad_list(ys, len(xs), 0)
        else:
            xs = pad_list(xs, len(ys), 0)
    assert len(xs) == len(ys)

    sums: list[int] = []
    idx: int = 0
    while idx < len(xs):
        sums.append(xs[idx] + ys[idx])
        idx += 1
    return sums

    # sums: list[int] = pad_list([], len(xs), 0)
    # idx: int = 0
    # while idx < len(xs):
    #     sums[idx] = xs[idx] + ys[idx]
    #     idx += 1
    # return sums

    # sums: list[int] = []
    # idx: int = 0
    # while idx < len(xs) or idx < len(ys):
    #     if idx < len(xs) and idx < len(ys):
    #         sums.append(xs[idx] + ys[idx])
    #     elif idx < len(xs):
    #         sums.append(xs[idx])
    #     else:
    #         sums.append(ys[idx])
    #     idx += 1
    # return sums
