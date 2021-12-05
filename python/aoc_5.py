from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int


@dataclass
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


def points_iter(lines: List[Line]):
    for line in lines:
        yield line.start
        yield line.end


def point_in_line(point: Point, line: Line) -> bool:
    if point.x == line.start.x and point.x == line.end.x:
        return min(line.start.y, line.end.y) <= point.y <= max(line.start.y, line.end.y)
    if point.y == line.start.y and point.y == line.end.y:
        return min(line.start.x, line.end.x) <= point.x <= max(line.start.x, line.end.x)
    return (
        abs(point.x - line.start.x) == abs(point.y - line.start.y)
        and min(line.start.y, line.end.y) <= point.y <= max(line.start.y, line.end.y)
        and min(line.start.x, line.end.x) <= point.x <= max(line.start.x, line.end.x)
    )


# Absolute naive brutforce point in the line checking.
def solve(lines: List[Line]) -> int:
    x_min = min(map(lambda p: p.x, points_iter(lines)))
    x_max = max(map(lambda p: p.x, points_iter(lines)))
    y_min = min(map(lambda p: p.y, points_iter(lines)))
    y_max = max(map(lambda p: p.y, points_iter(lines)))

    total = 0
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            point = Point(x, y)
            has_line = False
            for line in lines:
                if point_in_line(point, line):
                    if has_line:
                        total += 1
                        break
                    has_line = True

    return total


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
