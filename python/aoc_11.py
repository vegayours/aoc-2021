from typing import List, Tuple, Set
from functools import reduce


def read_input(lines: List[str]) -> List[List[int]]:
    return [[int(c) for c in line] for line in lines]


def neighbors(input: List[List[int]], i: int, j: int):
    m, n = len(input), len(input[0])
    for x, y in [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]:
        if 0 <= x < m and 0 <= y < n:
            yield x, y


def process(input: List[List[int]], i: int, j: int, flashed: Set[Tuple[int, int]]):
    if (i, j) in flashed:
        return

    input[i][j] += 1
    if input[i][j] > 9:
        flashed.add((i, j))
        input[i][j] = 0
        for x, y in neighbors(input, i, j):
            process(input, x, y, flashed)


def make_step(input: List[List[int]]):
    flashed = set()
    for i, row in enumerate(input):
        for j, _ in enumerate(input):
            process(input, i, j, flashed)
    return len(flashed)


def solve_1(lines: List[str]):
    input = read_input(lines)
    return sum(make_step(input) for _ in range(100))


def solve_2(lines: List[str]):
    input = read_input(lines)
    step = 0
    while True:
        step += 1
        if make_step(input) == 100:
            return step


def solution():
    return {"1": solve_1, "2": solve_2}
