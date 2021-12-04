from functools import reduce
from collections import namedtuple, defaultdict
from typing import List, Tuple, Dict
import typing


class Board(object):
    def __init__(self):
        self.rows = []
        self.state = []
        self.row_count = []
        self.col_count = []
        self.num_positions = defaultdict(list)

    def add_row(self, row):
        self.rows.append(row)
        self.state.append([False for _ in range(len(row))])

        self.row_count.append(0)
        if not self.col_count:
            self.col_count = [0 for _ in range(len(row))]

        row_pos = len(self.rows) - 1
        for (col_pos, value) in enumerate(row):
            self.num_positions[value].append((row_pos, col_pos))

    def is_complete(self):
        return any(cnt == len(self.rows) for cnt in self.row_count) or any(
            cnt == len(self.rows[0]) for cnt in self.col_count
        )

    def score(self):
        score = 0
        for row_pos, row_state in enumerate(self.state):
            for col_pos, marked in enumerate(row_state):
                if not marked:
                    score += self.rows[row_pos][col_pos]
        return score

    def add_number(self, num):
        for row_pos, col_pos in self.num_positions[num]:
            if not self.state[row_pos][col_pos]:
                self.state[row_pos][col_pos] = True
                self.row_count[row_pos] += 1
                self.col_count[col_pos] += 1

    def __str__(self):
        return "{}\n{}\n{}\n{}".format(
            self.rows, self.state, self.row_count, self.col_count
        )


def process_line(boards: List[Board], line: str) -> List[Board]:
    if len(line) == 0:
        boards.append(Board())
    else:
        boards[-1].add_row([int(x.strip()) for x in line.split()])
    return boards


def read_input(lines: List[str]) -> Tuple[List[int], List[Board]]:
    nums = [int(x) for x in lines[0].split(",")]
    boards = reduce(process_line, lines[1:], [])
    return nums, boards


def solve_1(lines: List[str]) -> int:
    nums, boards = read_input(lines)
    for num in nums:
        for board in boards:
            board.add_number(num)
            if board.is_complete():
                return num * board.score()
    raise Exception("Problem has no solution")


def solve_2(lines):
    nums, boards = read_input(lines)
    playing_boards = boards
    for num in nums:
        next_boards = []
        for board in playing_boards:
            board.add_number(num)
            if not board.is_complete():
                next_boards.append(board)
            elif len(playing_boards) == 1:
                return playing_boards[0].score() * num
        playing_boards = next_boards
    raise Exception("Problem has no solution")


def solution():
    return {"1": solve_1, "2": solve_2}
