from typing import List, Tuple, cast
from dataclasses import dataclass
from math import prod


class BitReader(object):
    def __init__(self, hex):
        self.bits = "".join("{0:04b}".format(int(c, 16)) for c in hex)
        self.pos = 0

    def read_str(self, n_bits) -> str:
        if self.pos + n_bits > len(self.bits):
            raise ValueError("Not enough bits in the input string.")
        value = self.bits[self.pos : self.pos + n_bits]
        self.pos += n_bits
        return value

    def read_int(self, n_bits) -> int:
        return int(self.read_str(n_bits), 2)


def read_input(lines: List[str]) -> BitReader:
    return BitReader(lines[0])


@dataclass
class Chunk:
    version: int
    type_id: int


@dataclass
class Literal(Chunk):
    value: int


@dataclass
class Operator(Chunk):
    children: List[Chunk]


def parse_ast(reader: BitReader) -> Tuple[int, Chunk]:
    consumed_bits = 0

    def read_int(n_bits):
        nonlocal consumed_bits
        consumed_bits += n_bits
        return reader.read_int(n_bits)

    def read_str(n_bits):
        nonlocal consumed_bits
        consumed_bits += n_bits
        return reader.read_str(n_bits)

    version = read_int(3)
    type_id = read_int(3)

    if type_id == 4:
        literal_str = ""
        has_more = True
        while has_more:
            has_more = bool(read_int(1))
            literal_str += read_str(4)
        return consumed_bits, Literal(version, type_id, int(literal_str, 2))
    else:
        children = []
        if read_int(1) == 0:
            l = read_int(15)
            while l > 0:
                child_bits, chunk = parse_ast(reader)
                consumed_bits += child_bits
                l -= child_bits
                assert l >= 0
                children.append(chunk)
        else:
            n = read_int(11)
            for _ in range(n):
                child_bits, chunk = parse_ast(reader)
                consumed_bits += child_bits
                children.append(chunk)
        return consumed_bits, Operator(version, type_id, children)


def count_versions(node: Chunk):
    result = node.version
    if isinstance(node, Operator):
        result += sum(map(count_versions, cast(Operator, node).children))
    return result


OPERATORS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda args: int(args[0] > args[1]),
    6: lambda args: int(args[0] < args[1]),
    7: lambda args: int(args[0] == args[1]),
}


def evaluate(node: Chunk):
    if isinstance(node, Literal):
        return cast(Literal, node).value
    op = cast(Operator, node)
    children = [evaluate(child) for child in op.children]
    if op.type_id in OPERATORS:
        return OPERATORS[op.type_id](children)
    else:
        raise ValueError("Unsupported operator: {}".format(op))


def solve_1(lines: List[str]):
    reader = read_input(lines)
    _, ast = parse_ast(reader)
    return count_versions(ast)


def solve_2(lines: List[str]):
    reader = read_input(lines)
    _, ast = parse_ast(reader)
    return evaluate(ast)


def solution():
    return {"1": solve_1, "2": solve_2}
