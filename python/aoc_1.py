from itertools import tee


def iterate_tuples(iterable, n):
    sequences = tee(iterable, n)
    for i in range(len(sequences)):
        for _ in range(i):
            next(sequences[i])
    return zip(*sequences)


def count_greater_than_prev(pairs):
    return sum(map(lambda t: t[1] > t[0], pairs))


def solve_1(lines):
    nums = map(int, lines)
    pairs = iterate_tuples(nums, 2)
    return count_greater_than_prev(pairs)


def solve_2(lines):
    nums = map(int, lines)
    triplets = iterate_tuples(nums, 3)
    window_nums = map(sum, triplets)
    window_pairs = iterate_tuples(window_nums, 2)
    return count_greater_than_prev(window_pairs)


def solution():
    return {"1": solve_1, "2": solve_2}
