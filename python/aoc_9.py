from heapq import heappop, heappush
from typing import Dict, List, Tuple
from collections import defaultdict, deque
from heapq import heappush, heappop
from functools import reduce


def read_input(lines: List[str]) -> List[List[int]]:
    return [[int(x) for x in line] for line in lines]


def neighbors(x, y, input):
    m, n = len(input), len(input[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in dirs:
        i, j = x + dx, y + dy
        if 0 <= i < m and 0 <= j < n:
            yield i, j


def solve_1(lines: List[str]):
    input = read_input(lines)
    result = 0
    for i, row in enumerate(input):
        for j, value in enumerate(row):
            if all(input[x][y] > value for x, y in neighbors(i, j, input)):
                result += 1 + value
    return result


def component_size(
    input: List[List[int]], row: int, col: int, visited: Dict[Tuple[int, int], bool]
) -> int:
    size = 1
    q = []
    visited[row, col] = True
    q.append((row, col))
    while q:
        x, y = q.pop()
        for i, j in neighbors(x, y, input):
            if not visited[i, j] and input[i][j] != 9:
                size += 1
                visited[i, j] = True
                q.append((i, j))
    return size


def solve_2(lines: List[str]):
    input = read_input(lines)
    visited = defaultdict(bool)
    max_3 = []
    for i, row in enumerate(input):
        for j, value in enumerate(row):
            if not visited[i, j] and value != 9:
                size = component_size(input, i, j, visited)
                heappush(max_3, size)
                if len(max_3) > 3:
                    heappop(max_3)
    return reduce(lambda x, y: x * y, max_3, 1)


def solution():
    return {"1": solve_1, "2": solve_2}
