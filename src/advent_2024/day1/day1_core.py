from collections import Counter
from pathlib import Path


IN_PATH = Path.cwd() / "src/advent_2024/day1/data/input.txt"


def part1() -> int:
    left, right = parse_lists(IN_PATH)
    total_diff = sum_of_distances(left, right)
    return total_diff


def part2() -> int:
    left, right = parse_lists(IN_PATH)
    score = similarity_score(left, right)
    return score


def parse_lists(path: Path) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    with path.open() as in_file:
        for line in in_file:
            a, b = line.strip().split()
            left.append(int(a))
            right.append(int(b))

    return (left, right)


def sum_of_distances(left: list[int], right: list[int]) -> int:
    return sum(
        map(
            lambda a, b: abs(a - b),
            sorted(left),
            sorted(right),
        )
    )


def similarity_score(left: list[int], right: list[int]) -> int:
    right_counts = Counter(right)
    return sum(
        map(
            lambda elem: elem * right_counts.get(elem, 0),
            left,
        )
    )
