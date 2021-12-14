from typing import Dict, List, Sequence, Tuple
from collections import defaultdict


def get_coord(s: str):
    x, y = map(int, s.split(","))
    return x, y


def get_fold(s: str):
    fold = s.split(" ")[-1]
    c, value = fold.split("=")
    return c, int(value)


def read_input(lines: List[str]) -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    separator = lines.index("")
    coords_list = lines[:separator]
    folds_list = lines[separator + 1 :]
    coords = [get_coord(s) for s in coords_list]
    folds = [get_fold(s) for s in folds_list]
    return coords, folds


def translate_coord(coord: Tuple[int, int], fold: Tuple[str, int]):
    x, y = coord
    c, value = fold
    if c == "x":
        if x > value:
            x = 2 * value - x
    elif c == "y":
        if y > value:
            y = 2 * value - y
    return x, y


def fold_coords(coords: Dict[Tuple[int, int], int], fold: Tuple[str, int]):
    folded = defaultdict(int)
    for coord in coords:
        folded[translate_coord(coord, fold)] += 1
    return folded


def show_coords(coords: Dict[Tuple[int, int], int]):
    cols = max(x for x, _ in coords)
    rows = max(y for _, y in coords)
    grid = [["." for _ in range(cols + 1)] for _ in range(rows + 1)]
    for x, y in coords:
        grid[y][x] = "#"
    return "\n".join(("".join(row) for row in grid))


def solve_1(lines: List[str]):
    coords, folds = read_input(lines)
    sheet = {coord: 1 for coord in coords}
    return len(fold_coords(sheet, folds[0]))


def solve_2(lines: List[str]):
    coords, folds = read_input(lines)
    sheet = {coord: 1 for coord in coords}
    for fold in folds:
        sheet = fold_coords(sheet, fold)
    print(show_coords(sheet))


def solution():
    return {"1": solve_1, "2": solve_2}
