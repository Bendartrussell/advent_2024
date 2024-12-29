from itertools import chain
from operator import mul
import re


Mul = tuple[int, int]


def part1(data: str) -> int:
    instructions = extract_mul(data)
    result = calculate(instructions)
    return result


def part2(data: str) -> int:
    filtered = drop_disabled(data)
    instructions: list[Mul] = list(chain(*(extract_mul(seq) for seq in filtered)))
    result = calculate(instructions)
    return result


def extract_mul(data: str) -> list[Mul]:
    matches: list[Mul] = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return [
        (int(a), int(b)) for a, b in matches
    ]


def drop_disabled(data: str) -> list[str]:
    enabled_sequences: list[str] = []
    state: bool = True

    sequences: list[str] = re.split(r"don't\(\)", data)
    while sequences:
        next_seq = sequences.pop(0)
        if state:
            enabled_sequences.append(next_seq)
            state = False
        else:
            subsequences: list[str] = re.split(r"do\(\)", next_seq)
            if len(subsequences) > 1:
                enabled_sequences.extend(subsequences[1:])

    return enabled_sequences


def calculate(instructions: list[Mul]) -> int:
    return sum(map(
        lambda pair: mul(*pair),
        instructions,
    ))
