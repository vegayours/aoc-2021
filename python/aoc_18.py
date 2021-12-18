from typing import List
import json


def read_input(lines: List[str]):
    return [json.loads(l) for l in lines]


def to_flat(num):
    result = []

    def to_flat_rec(num, cur_depth):
        if isinstance(num, int):
            result.append([num, cur_depth])
        elif isinstance(num, list):
            for elem in num:
                to_flat_rec(elem, cur_depth + 1)

    to_flat_rec(num, 0)
    return result


def to_num(flat):
    depth = 1
    result = []
    num = [result]
    for val, d in flat:
        while depth < d:
            l = []
            num[-1].append(l)
            num.append(l)
            depth += 1
        while depth > d:
            num.pop()
            depth -= 1
        num[-1].append(val)
        while num and len(num[-1]) == 2:
            num.pop()
            depth -= 1
    return result


def explode(flat):
    for index, ((a_val, a_d), (b_val, b_d)) in enumerate(zip(flat, flat[1:])):
        if a_d == b_d and a_d > 4:
            if index > 0:
                flat[index - 1][0] += a_val
            if index + 2 < len(flat):
                flat[index + 2][0] += b_val
            flat[index + 1] = [0, a_d - 1]
            flat.pop(index)
            return True
    return False


def split(flat):
    for index, (val, d) in enumerate(flat):
        if val >= 10:
            flat[index] = [val // 2, d + 1]
            flat.insert(index + 1, [(val + 1) // 2, d + 1])
            return True
    return False


def reduce(flat):
    while explode(flat) or split(flat):
        pass
    return flat


def magnitude(num):
    if isinstance(num, int):
        return num
    else:
        a, b = num
        return magnitude(a) * 3 + magnitude(b) * 2


def solve_1(lines: List[str]):
    nums = read_input(lines)
    acc = nums[0]
    for num in nums[1:]:
        acc = to_num(reduce(to_flat([acc, num])))
    return magnitude(acc)


def solve_2(lines: List[str]):
    nums = read_input(lines)
    best = 0
    for index_1, num_1 in enumerate(nums):
        for index_2, num_2 in enumerate(nums):
            if index_1 != index_2:
                s = to_num(reduce(to_flat([num_1, num_2])))
                best = max(best, magnitude(s))
    return best


def solution():
    return {"1": solve_1, "2": solve_2}
