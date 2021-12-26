from typing import List, Tuple
import dataclasses
from itertools import islice, product
from functools import cache
from collections import Counter


DIRAC_DICE_CNT = Counter(map(sum, product(*[[1, 2, 3]] * 3)))


@dataclasses.dataclass(eq=True, frozen=True)
class Player:
    pos: int
    score: int = 0


def advance(self: Player, delta) -> Player:
    pos = (self.pos + delta - 1) % 10 + 1
    score = self.score + pos
    return Player(pos, score)


def read_player(line: str) -> Player:
    return Player(pos=int(line.split(" ")[4]))


def read_input(lines: List[str]) -> Tuple[Player, Player]:
    return read_player(lines[0]), read_player(lines[1])


def make_dice(limit):
    while True:
        yield from range(1, limit + 1)


def solve_1(lines: List[str]):
    p1, p2 = read_input(lines)
    dice = make_dice(100)
    moves = 0
    while True:
        delta = sum(islice(dice, 3))
        moves += 3
        p1 = advance(p1, delta)
        if p1.score >= 1000:
            return p2.score * moves
        p1, p2 = p2, p1


@cache
def count_wins(p1: Player, p2: Player, cnt: int) -> Tuple[int, int]:
    r1, r2 = 0, 0
    for val, c in DIRAC_DICE_CNT.items():
        p1_c = advance(p1, val)
        if p1_c.score >= 21:
            r1 += cnt * c
        else:
            r2_c, r1_c = count_wins(p2, p1_c, cnt * c)
            r1 += r1_c
            r2 += r2_c
    return r1, r2


def solve_2(lines: List[str]):
    p1, p2 = read_input(lines)
    return max(count_wins(p1, p2, 1))


def solution():
    return {"1": solve_1, "2": solve_2}
