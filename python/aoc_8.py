from typing import List, Tuple


def parse_input(lines: List[str]) -> List[Tuple[List[str], List[str]]]:
    parts = [line.split(" | ") for line in lines]
    return [(part[0].split(), part[1].split()) for part in parts]


def match_diff(candidate, pattern):
    return len(set(pattern)) - len(set(candidate).intersection(set(pattern)))


def matches(candidate, pattern):
    return match_diff(candidate, pattern) == 0


def is_0(pattern, context):
    return (
        len(pattern) == 6
        and matches(pattern, context["1"])
        and not matches(pattern, context["4"])
    )


def is_1(pattern, context):
    return len(pattern) == 2


def is_2(pattern, context):
    return len(pattern) == 5 and match_diff(pattern, context["4"]) == 2


def is_3(pattern, context):
    return len(pattern) == 5 and matches(pattern, context["1"])


def is_4(pattern, context):
    return len(pattern) == 4


def is_5(pattern, context):
    return (
        len(pattern) == 5
        and not matches(pattern, context["1"])
        and match_diff(pattern, context["4"]) == 1
    )


def is_6(pattern, context):
    return (
        len(pattern) == 6
        and not matches(pattern, context["1"])
        and not matches(pattern, context["4"])
    )


def is_7(pattern, context):
    return len(pattern) == 3


def is_8(pattern, context):
    return len(pattern) == 7


def is_9(pattern, context):
    return len(pattern) == 6 and matches(pattern, context["4"])


def decode_measurements(input):
    predicates = [
        (is_0, "0"),
        (is_1, "1"),
        (is_2, "2"),
        (is_3, "3"),
        (is_4, "4"),
        (is_5, "5"),
        (is_6, "6"),
        (is_7, "7"),
        (is_8, "8"),
        (is_9, "9"),
    ]

    def matching_num(pattern, context):
        for predicate, result in predicates:
            if predicate(pattern, context):
                return result
        raise ValueError(
            "No valid predicate for pattern: {}, context: {}".format(pattern, context)
        )

    result = []
    for left, right in input:
        patterns = left + right
        context = {}
        for pattern in patterns:
            if len(pattern) in (2, 3, 4):
                context[matching_num(pattern, context)] = pattern
        result.append(list(map(lambda pattern: matching_num(pattern, context), right)))
    return result


def solve_1(lines: List[str]):
    input = parse_input(lines)
    results = decode_measurements(input)
    return sum(sum(x in ("1", "4", "7", "8") for x in entry) for entry in results)


def solve_2(lines: List[str]):
    input = parse_input(lines)
    results = decode_measurements(input)
    return sum(int("".join(entry)) for entry in results)


def solution():
    return {"1": solve_1, "2": solve_2}
