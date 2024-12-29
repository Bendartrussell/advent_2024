from operator import mul
import re


Mul = tuple[int, int]


def part1(data: str) -> int:
    instructions = extract_mul(data)
    result = calculate(instructions)
    return result


def part2(data: str) -> int:
    return 1


def extract_mul(data: str) -> list[Mul]:
    matches: list[Mul] = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    return [
        (int(a), int(b)) for a, b in matches
    ]


def calculate(instructions: list[Mul]) -> int:
    return sum(map(
        lambda pair: mul(*pair),
        instructions,
    ))
