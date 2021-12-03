from collections import Counter


def solve_1(lines):
    n_pos = len(lines[0])
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(n_pos):
        cnt = Counter(l[i] for l in lines)
        if cnt["1"] > cnt["0"]:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def find_rating(lines, inverse):
    n_pos = len(lines[0])
    candidates = set(lines)

    for i in range(n_pos):
        n_candidates = len(candidates)
        if n_candidates == 1:
            break

        cnt = Counter(l[i] for l in candidates)

        if cnt["1"] >= cnt["0"]:
            target = True
        else:
            target = False
        if inverse:
            target = not target

        next_candidates = set()
        for line in candidates:
            if (line[i] == "1") == target:
                next_candidates.add(line)
        candidates = next_candidates

    if len(candidates) != 1:
        raise AssertionError(
            "Expected exactly 1 candidaets, got: {}".format(candidates)
        )
    return candidates.pop()


def solve_2(lines):
    oxygen = find_rating(lines, inverse=False)
    co2 = find_rating(lines, inverse=True)
    return int(oxygen, 2) * int(co2, 2)


def solution():
    return {"1": solve_1, "2": solve_2}
