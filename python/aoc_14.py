from collections import defaultdict
from typing import Dict, List, Tuple

Substitutions = Dict[str, Tuple[str, List[str]]]
InputState = Tuple[Dict[str, int], Dict[str, int], Substitutions]


def read_input(
    lines: List[str],
) -> InputState:
    pairs = defaultdict(int)
    common = defaultdict(int)
    substitutions = dict()

    initial = lines[0]
    for (a, b) in zip(initial, initial[1:]):
        pairs[a + b] += 1
    for c in initial[1:-1]:
        common[c] += 1

    for l in lines[2:]:
        s, c = l.split(" -> ")
        substitutions[s] = (c, [s[0] + c, c + s[1]])

    return pairs, common, substitutions


def substitute(input: InputState) -> InputState:
    pairs, common, substitutions = input
    next_pairs = defaultdict(int)
    next_common = common.copy()

    for pair, count in pairs.items():
        if pair in substitutions:
            c, new_pairs = substitutions[pair]
            for p in new_pairs:
                next_pairs[p] += count
            next_common[c] += count
        else:
            next_pairs[pair] += count

    return next_pairs, next_common, substitutions


def char_count(input: InputState):
    pairs, common, _ = input
    cnt = defaultdict(int)
    for pair, count in pairs.items():
        for c in pair:
            cnt[c] += count
    for c, count in common.items():
        cnt[c] -= count
    return cnt


def solve(lines: List[str], iterations: int):
    input = read_input(lines)
    for _ in range(iterations):
        input = substitute(input)
    cnt = char_count(input)
    return max(cnt.values()) - min(cnt.values())


def solve_1(lines: List[str]):
    return solve(lines, 10)


def solve_2(lines: List[str]):
    return solve(lines, 40)


def solution():
    return {"1": solve_1, "2": solve_2}
