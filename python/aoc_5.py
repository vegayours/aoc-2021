from dataclasses import dataclass
from typing import List, Set
from collections import Counter

# from functools import cached_property


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point


def parse_line(input: str) -> Line:
    start, _, end = input.split()
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return Line(Point(int(x1), int(y1)), Point(int(x2), int(y2)))


def parse_lines(input: List[str]) -> List[Line]:
    return list(map(parse_line, input))


def coord_delta(first: int, second: int) -> int:
    if first == second:
        return 0
    elif first < second:
        return 1
    else:
        return -1


def line_points(line: Line):
    dx = coord_delta(line.start.x, line.end.x)
    dy = coord_delta(line.start.y, line.end.y)

    steps = max(abs(line.start.x - line.end.x), abs(line.start.y - line.end.y))

    point = line.start
    for _ in range(steps):
        yield point
        point = Point(point.x + dx, point.y + dy)
    yield point


def solve(lines: List[Line]) -> int:
    count = Counter(p for l in lines for p in line_points(l))
    return sum(x > 1 for x in count.values())


def solve_1(input: List[str]):
    lines = parse_lines(input)
    valid_lines = [
        line
        for line in lines
        if line.start.x == line.end.x or line.start.y == line.end.y
    ]
    return solve(valid_lines)


def solve_2(input: List[str]):
    lines = parse_lines(input)
    return solve(lines)


def solution():
    return {"1": solve_1, "2": solve_2}
