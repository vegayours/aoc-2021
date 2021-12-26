from typing import Generator, List
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Range:
    start: int
    end: int

    def value(self):
        return max(0, self.end - self.start)


@dataclass(eq=True, frozen=True)
class Cube:
    x: Range
    y: Range
    z: Range

    def value(self):
        return self.x.value() * self.y.value() * self.z.value()


@dataclass
class Step:
    on: bool
    cube: Cube


def parse_range(s: str) -> Range:
    start, end = s[2:].split("..")
    return Range(int(start), int(end) + 1)


def parse_step(s: str) -> Step:
    on_str, cube_str = s.split(" ")
    x_range, y_range, z_range = cube_str.split(",")
    return Step(
        on=on_str == "on",
        cube=Cube(parse_range(x_range), parse_range(y_range), parse_range(z_range)),
    )


def read_steps(lines: List[str]) -> List[Step]:
    return [parse_step(l) for l in lines]


def range_intersection(left: Range, right: Range):
    return Range(max(left.start, right.start), min(left.end, right.end))


def cube_intersection(left: Cube, right: Cube) -> Cube:
    return Cube(
        range_intersection(left.x, right.x),
        range_intersection(left.y, right.y),
        range_intersection(left.z, right.z),
    )


def iterate_ranges(r1: Range, r2: Range):
    bounds = [
        min(r1.start, r2.start),
        max(r1.start, r2.start),
        min(r1.end, r2.end),
        max(r1.end, r2.end),
    ]
    for start, end in zip(bounds, bounds[1:]):
        yield Range(start, end)


def filter_cubes(left: Cube, right: Cube) -> Generator[Cube, None, None]:
    for x_r in iterate_ranges(left.x, right.x):
        for y_r in iterate_ranges(left.y, right.y):
            for z_r in iterate_ranges(left.z, right.z):
                c = Cube(x_r, y_r, z_r)
                if (
                    c.value() > 0
                    and cube_intersection(c, left).value() > 0
                    and cube_intersection(c, right).value() == 0
                ):
                    yield c


def process_step(on_cubes: List[Cube], step: Step) -> List[Cube]:
    cubes = []
    for on_cube in on_cubes:
        intersection = cube_intersection(on_cube, step.cube)
        if intersection.value() == 0:
            cubes.append(on_cube)
        elif intersection.value() != on_cube:
            for c in filter_cubes(on_cube, step.cube):
                cubes.append(c)

    if step.on:
        cubes.append(step.cube)
    return cubes


def part1_steps(steps: List[Step]):
    limit_range = Range(-50, 51)
    limit_cube = Cube(limit_range, limit_range, limit_range)

    for step in steps:
        intersection = cube_intersection(limit_cube, step.cube)
        if intersection.value() > 0:
            yield Step(step.on, intersection)


def solve(steps: List[Step]):
    on_cubes = []
    for step in steps:
        on_cubes = process_step(on_cubes, step)

    return sum(cube.value() for cube in on_cubes)


def solve_1(lines: List[str]):
    steps = read_steps(lines)
    return solve(list(part1_steps(steps)))


def solve_2(lines: List[str]):
    steps = read_steps(lines)
    return solve(steps)


def solution():
    return {"1": solve_1, "2": solve_2}
