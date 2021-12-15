from typing import List, Tuple
from heapq import heappush, heappop


def read_input(lines: List[str]) -> List[List[int]]:
    return [[int(c) for c in l] for l in lines]


def neighbors4(grid: List[List[int]], point: Tuple[int, int]):
    m, n = len(grid), len(grid[0])
    x, y = point
    if x > 0:
        yield x - 1, y
    if x + 1 < m:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y + 1 < n:
        yield x, y + 1


def shortest_path(
    grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> int:
    cost = {start: 0}
    pq = [(0, start)]
    while pq:
        c, point = heappop(pq)
        if cost[point] > c:
            continue
        for n in neighbors4(grid, point):
            n_cost = c + grid[n[0]][n[1]]
            if n not in cost or cost[n] > n_cost:
                cost[n] = n_cost
                heappush(pq, (n_cost, n))
                if n == end:
                    break
    return cost[end]


def expand_grid(grid, scale):
    m, n = len(grid), len(grid[0])

    expanded_grid = [[0 for _ in range(scale * n)] for _ in range(scale * m)]

    for i in range(scale * m):
        for j in range(scale * n):
            expanded_grid[i][j] = (grid[i % m][j % n] - 1 + i // m + j // n) % 9 + 1

    return expanded_grid


def solve(grid: List[List[int]]):
    m, n = len(grid), len(grid[0])
    return shortest_path(grid, (0, 0), (m - 1, n - 1))


def solve_1(lines: List[str]):
    grid = read_input(lines)
    return solve(grid)


def solve_2(lines: List[str]):
    grid = expand_grid(read_input(lines), 5)
    return solve(grid)


def solution():
    return {"1": solve_1, "2": solve_2}
