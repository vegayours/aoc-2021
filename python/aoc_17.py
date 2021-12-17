from typing import List, Tuple
from math import sqrt, ceil
from functools import cache


def read_input(lines: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    l = lines[0][len("target area: ") :]
    x_part, y_part = l.split(", ")
    x1, x2 = (int(x) for x in x_part[2:].split(".."))
    y1, y2 = (int(y) for y in y_part[2:].split(".."))
    return (x1, x2), (y1, y2)


def get_x_min(x_lim):
    return ceil(sqrt(2 * min(x_lim) + 0.25) - 0.5)


def out_bounds(x, y, x_v, x_lim, y_lim):
    return y < min(y_lim) or x > max(x_lim)


def simulate(x_v, y_v, x_lim, y_lim):
    x, y = x_v, y_v
    while not out_bounds(x, y, x_v, x_lim, y_lim):
        yield x, y

        if x_v > 0:
            x_v -= 1
        elif x_v < 0:
            x_v += 1
        y_v -= 1

        x += x_v
        y += y_v


def evaluate(x_v, y_v, x_lim, y_lim):
    within = False
    y_max = min(y_lim)
    for x, y in simulate(x_v, y_v, x_lim, y_lim):
        if min(x_lim) <= x <= max(x_lim) and min(y_lim) <= y <= max(y_lim):
            within = True
        y_max = max(y_max, y)
    return within, y_max


@cache
def count_velocities(x_lim, y_lim):
    x_min, x_max = get_x_min(x_lim), max(x_lim)
    y_min, y_max = min(y_lim), -(min(y_lim) + 1)

    max_h = min(y_lim)
    cnt = 0
    for x_v in range(x_min, x_max + 1):
        for y_v in range(y_min, y_max + 1):
            within, h = evaluate(x_v, y_v, x_lim, y_lim)
            if within:
                cnt += 1
                max_h = max(max_h, h)
    return cnt, max_h


def solve_1(lines: List[str]):
    x_lim, y_lim = read_input(lines)
    _, max_h = count_velocities(x_lim, y_lim)
    return max_h


def solve_2(lines: List[str]):
    x_lim, y_lim = read_input(lines)
    cnt, _ = count_velocities(x_lim, y_lim)
    return cnt


def solution():
    return {"1": solve_1, "2": solve_2}
