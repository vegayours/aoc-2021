from typing import List
from statistics import median
from functools import reduce

OPEN_MATCHES = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSE_MATCHES = dict((v, k) for k, v in OPEN_MATCHES.items())

PART1_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
PART2_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def parse_navigation(line: str):
    stack = []
    for c in line:
        if c in OPEN_MATCHES:
            stack.append(c)
        else:
            if not stack or CLOSE_MATCHES[c] != stack[-1]:
                return [], c
            else:
                stack.pop()
    return stack, None


def solve_1(lines: List[str]):
    navigations = map(parse_navigation, lines)
    corrupted = (PART1_SCORE[paren] for _, paren in navigations if paren)
    return sum(corrupted)


def incomplete_score(parens: List[str]):
    completion = (OPEN_MATCHES[c] for c in reversed(parens))
    return reduce(lambda acc, c: acc * 5 + PART2_SCORE[c], completion, 0)


def solve_2(lines: List[str]):
    navigations = map(parse_navigation, lines)
    incomplete_scores = (incomplete_score(s) for s, _ in navigations if s)
    return median(incomplete_scores)


def solution():
    return {"1": solve_1, "2": solve_2}
