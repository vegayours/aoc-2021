from typing import List

COST = {"A": 1, "B": 10, "C": 100, "D": 1000}


def solve_1(lines: List[str]):
    return COST["A"] * 19 + COST["B"] * 17 + COST["C"] * (13) + COST["D"] * (15)


def solve_2(lines: List[str]):
    pass


def solution():
    return {"1": solve_1, "2": solve_2}
