from pathlib import Path

from advent_2024.day1 import part1, part2


def test_part1_example():
    example_data = (
        "3   4\n"
        "4   3\n"
        "2   5\n"
        "1   3\n"
        "3   9\n"
        "3   3\n"
    )
    assert part1(example_data) == 11


def test_part1():
    in_path = Path().cwd() / "test/unit/day1/data/input.txt"
    with in_path.open() as in_file:
        assert part1(in_file.read()) == 1530215


def test_part2_example():
    example_data = (
        "3   4\n"
        "4   3\n"
        "2   5\n"
        "1   3\n"
        "3   9\n"
        "3   3\n"
    )
    assert part2(example_data) == 31


def test_part2():
    in_path = Path().cwd() / "test/unit/day1/data/input.txt"
    with in_path.open() as in_file:
        assert part2(in_file.read()) == 26800609
