from argparse import ArgumentParser
from os import path

import aoc_1
import aoc_2
import aoc_3
import aoc_4
import aoc_5
import aoc_6
import aoc_7
import aoc_8
import aoc_9
import aoc_10
import aoc_11
import aoc_12
import aoc_13
import aoc_14
import aoc_15
import aoc_16
import aoc_17

SOLUTIONS = {
    "1": aoc_1.solution(),
    "2": aoc_2.solution(),
    "3": aoc_3.solution(),
    "4": aoc_4.solution(),
    "5": aoc_5.solution(),
    "6": aoc_6.solution(),
    "7": aoc_7.solution(),
    "8": aoc_8.solution(),
    "9": aoc_9.solution(),
    "10": aoc_10.solution(),
    "11": aoc_11.solution(),
    "12": aoc_12.solution(),
    "13": aoc_13.solution(),
    "14": aoc_14.solution(),
    "15": aoc_15.solution(),
    "16": aoc_16.solution(),
    "17": aoc_17.solution(),
}


def read_input(input_dir, mod):
    filename = path.join(input_dir, "aoc_{}.txt".format(mod))
    return read_file(filename)


def read_file(filename):
    with open(filename, "r") as f:
        return [l.rstrip("\n") for l in f.readlines()]


def get_solve_fn(mod, part):
    if mod not in SOLUTIONS:
        raise ValueError("Solution for task {} is not supported.".format(mod))
    solution = SOLUTIONS[mod]
    if part not in solution:
        raise ValueError("Part {} for task {} is not supported.".format(part))
    return solution[part]


def main(args):
    if not args.tasks:
        for day, day_solver in SOLUTIONS.items():
            input = read_input(args.input_dir, day)
            for part, solve_fn in day_solver.items():
                result = solve_fn(input)
                print("Task: {}_{}, solution: {}".format(day, part, result))
        return

    for task in args.tasks[0]:
        mod, part = task.split("_")
        solve_fn = get_solve_fn(mod, part)
        input = read_input(args.input_dir, mod)
        result = solve_fn(input)
        print("Task: {}, solution: {}".format(task, result))


if __name__ == "__main__":
    parser = ArgumentParser(description="Advent of Code 2021 solutions.")
    parser.add_argument(
        "--tasks",
        nargs="+",
        type=str,
        action="append",
        help="Tasks to execute, e.g. --tasks 1_1 1_2  3_1 etc.",
    )
    parser.add_argument(
        "--input-dir",
        type=str,
        default="../input",
        help="Base directory with input files.",
    )
    args = parser.parse_args()
    main(args)
