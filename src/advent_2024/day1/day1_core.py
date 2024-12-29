from collections import Counter


def part1(data: str) -> int:
    left, right = parse_lists(data)
    total_diff = sum_of_distances(left, right)
    return total_diff


def part2(data: str) -> int:
    left, right = parse_lists(data)
    score = similarity_score(left, right)
    return score


def parse_lists(data: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []

    for line in data.strip().split("\n"):
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
