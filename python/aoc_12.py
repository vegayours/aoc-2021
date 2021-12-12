from typing import Dict, List, Set
from collections import defaultdict


def read_graph(lines: List[str]) -> Dict[str, Set[str]]:
    graph = defaultdict(set)
    for l in lines:
        i, j = l.split("-")
        graph[i].add(j)
        graph[j].add(i)
    return graph


def backtrack(i: str, g: Dict[str, Set[str]], count: Dict[str, int], max_count):
    if i == "end":
        return 1
    result = 0
    for j in g[i]:
        if count[j] >= max_count:
            continue
        if j.islower():
            count[j] += 1
        result += backtrack(
            j, g, count, min(max_count, 1 if count[j] >= max_count else max_count)
        )
        if j.islower():
            count[j] -= 1
    return result


def solve_1(lines: List[str]):
    g = read_graph(lines)
    count = defaultdict(int)
    count["start"] = 2
    return backtrack("start", g, count, max_count=1)


def solve_2(lines: List[str]):
    g = read_graph(lines)
    count = defaultdict(int)
    count["start"] = 2
    return backtrack("start", g, count, max_count=2)


def solution():
    return {"1": solve_1, "2": solve_2}
