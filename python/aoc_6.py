from typing import List
from collections import deque


def parse_input(lines: List[str]) -> List[int]:
    return [int(x) for x in lines[0].split(",")]


def solve(input: List[int], days: int) -> int:
    age_count = deque([0 for _ in range(9)])
    for x in input:
        age_count[x] += 1
    for _ in range(days):
        new = age_count.popleft()
        age_count.append(new)
        age_count[6] += new
    return sum(age_count)


def solve_1(lines: List[str]):
    return solve(parse_input(lines), 80)


def solve_2(lines: List[str]):
    return solve(parse_input(lines), 256)


def solution():
    return {"1": solve_1, "2": solve_2}
