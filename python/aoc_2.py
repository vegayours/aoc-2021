from functools import reduce


def parse_move(move):
    direction, delta = move.split(" ")
    return direction, int(delta)


def process_move_1(current_pos, move):
    horizontal, depth = current_pos
    direction, delta = parse_move(move)
    if direction == "forward":
        horizontal += delta
    elif direction == "up":
        depth -= delta
    elif direction == "down":
        depth += delta
    return horizontal, depth


def process_move_2(current_pos, move):
    horizontal, depth, aim = current_pos
    direction, delta = parse_move(move)
    if direction == "forward":
        horizontal += delta
        depth += aim * delta
    elif direction == "up":
        aim -= delta
    elif direction == "down":
        aim += delta
    return horizontal, depth, aim


def solve_1(lines):
    horizontal, depth = reduce(process_move_1, lines, (0, 0))
    return horizontal * depth


def solve_2(lines):
    horizontal, depth, _ = reduce(process_move_2, lines, (0, 0, 0))
    return horizontal * depth


def solution():
    return {"1": solve_1, "2": solve_2}
