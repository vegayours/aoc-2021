from typing import List, Tuple
from functools import cache

Image = List[List[bool]]


def read_input(lines: List[str]) -> Tuple[str, Image]:
    enhancement = lines[0]
    assert (len(enhancement)) == 2 ** 9
    image = [[c == "#" for c in l] for l in lines[2:]]
    return enhancement, image


def shift_update(value, bit) -> int:
    return ((value << 1) | int(bit)) & 7


def get_index(dp: list[list[int]], i: int, j: int) -> int:
    return (dp[(i - 2) % 3][j] << 6) | (dp[(i - 1) % 3][j] << 3) | dp[i % 3][j]


def enhance_image(prev_image: Image, enhancement: str, fill: bool):
    rows, cols = len(prev_image), len(prev_image[0])
    image = [[fill for _ in range(cols + 2)] for _ in range(rows + 2)]

    dp = [[(7 if fill else 0) for _ in range(cols + 3)] for _ in range(3)]

    for i in range(rows + 2):
        for j in range(cols + 2):
            value = prev_image[i][j] if i < rows and j < rows else fill
            dp[(i + 2) % 3][j + 1] = shift_update(dp[(i + 2) % 3][j], value)
            image[i][j] = enhancement[get_index(dp, i + 2, j + 1)] == "#"

    return image


def solve(lines: List[str], steps):
    enhancement, image = read_input(lines)
    for i in range(steps):
        inverse = (enhancement[0] == "#") and (i % 2 == 1)
        image = enhance_image(image, enhancement, inverse)
    return sum(sum(row) for row in image)


def solve_1(lines: List[str]):
    return solve(lines, 2)


def solve_2(lines: List[str]):
    return solve(lines, 50)


def solution():
    return {"1": solve_1, "2": solve_2}
