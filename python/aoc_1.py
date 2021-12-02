from more_itertools import windowed


def count_greater_than_prev(pairs):
    return sum(map(lambda t: t[1] > t[0], pairs))


def solve_1(lines):
    nums = map(int, lines)
    pairs = windowed(nums, 2)
    return sum(map(lambda t: t[1] > t[0], pairs))  # type: ignore


def solve_2(lines):
    nums = map(int, lines)
    pairs = windowed(nums, 4)
    return sum(map(lambda t: t[3] > t[0], pairs))  # type: ignore


def solution():
    return {"1": solve_1, "2": solve_2}
