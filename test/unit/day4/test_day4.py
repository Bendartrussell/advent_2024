from pathlib import Path

from advent_2024.day4 import part1, part2


def test_part1_example():
    example_data = (
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX\n"
    )
    assert part1(example_data) == 18


def test_part1():
    in_path = Path().cwd() / "test/unit/day4/data/input.txt"
    with in_path.open() as in_file:
        assert part1(in_file.read()) == 2530


def test_part2_example():
    example_data = (
        "MMMSXXMASM\n"
        "MSAMXMSMSA\n"
        "AMXSXMAAMM\n"
        "MSAMASMSMX\n"
        "XMASAMXAMM\n"
        "XXAMMXXAMA\n"
        "SMSMSASXSS\n"
        "SAXAMASAAA\n"
        "MAMMMXMMMM\n"
        "MXMXAXMASX\n"
    )
    assert part2(example_data) == 9


def test_part2():
    in_path = Path().cwd() / "test/unit/day4/data/input.txt"
    with in_path.open() as in_file:
        assert part2(in_file.read()) == 1921
