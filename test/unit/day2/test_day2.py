from advent_2024.day2 import part1, part2


def test_part1_example():
    example_data = (
        "7 6 4 2 1\n"
        "1 2 7 8 9\n"
        "9 7 6 2 1\n"
        "1 3 2 4 5\n"
        "8 6 4 4 1\n"
        "1 3 6 7 9\n"
    )
    assert part1(example_data) == 2
