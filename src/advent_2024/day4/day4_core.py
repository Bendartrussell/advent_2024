from .cls_Wordsearch import Wordsearch


def part1(data: str) -> int:
    ws = Wordsearch(data)
    start_coords = ws.find_coords("X")
    return sum(ws.count_word_at("XMAS", coord) for coord in start_coords)


def part2(data: str) -> int:
    return 1
