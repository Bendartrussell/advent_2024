from pathlib import Path

from advent_2024.day3 import part1, part2


def test_part1_example():
    example_data = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert part1(example_data) == 161


def test_part1():
    in_path = Path().cwd() / "test/unit/day3/data/input.txt"
    with in_path.open() as in_file:
        assert part1(in_file.read()) == 175015740


def test_part2_example():
    example_data = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert part2(example_data) == 48


def test_part2():
    in_path = Path().cwd() / "test/unit/day3/data/input.txt"
    with in_path.open() as in_file:
        assert part2(in_file.read()) == 112272912
