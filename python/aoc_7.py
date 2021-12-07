from typing import List


def read_input(lines: List[str]) -> List[int]:
    return [int(x) for x in lines[0].split(",")]


def solve(positions: List[int], distance_fn) -> int:
    best = sum(distance_fn(x) for x in positions)
    for x in positions:
        current = 0
        for y in positions:
            current += distance_fn(abs(x - y))
        best = min(current, best)
    return best


def solve_1(lines: List[str]):
    return solve(read_input(lines), lambda x: x)


def solve_2(lines: List[str]):
    return solve(read_input(lines), lambda x: x * (x + 1) // 2)


def solution():
    return {"1": solve_1, "2": solve_2}
