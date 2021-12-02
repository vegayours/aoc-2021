from argparse import ArgumentParser
from os import path

import aoc_1
import aoc_2

SOLUTIONS = {"1": aoc_1.solution(), "2": aoc_2.solution()}


def read_input(input_dir, mod):
    filename = path.join(input_dir, "aoc_{}.txt".format(mod))
    return read_file(filename)


def read_file(filename):
    with open(filename, "r") as f:
        lines = [line for line in f.read().split("\n") if line]
    return lines


def get_solve_fn(mod, part):
    if mod not in SOLUTIONS:
        raise ValueError("Solution for task {} is not supported.".format(mod))
    solution = SOLUTIONS[mod]
    if part not in solution:
        raise ValueError("Part {} for task {} is not supported.".format(part))
    return solution[part]


def main(args):
    for task in args.tasks:
        mod, part = task.split("_")
        solve_fn = get_solve_fn(mod, part)
        input = read_input(args.input_dir, mod)
        result = solve_fn(input)
        print("Task: {}, solution: {}".format(task, result))


if __name__ == "__main__":
    parser = ArgumentParser(description="Advent of Code 2021 solutions.")
    parser.add_argument(
        "--tasks",
        type=str,
        nargs="+",
        action="extend",
        help="Tasks to execute, e.g. 1_1, 1_2, 3_1, etc.",
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        default="../input",
        help="Base directory with input files.",
    )
    args = parser.parse_args()
    main(args)
