from .cls_Wordsearch import Wordsearch


def part1(data: str) -> int:
    ws = Wordsearch(data)
    start_coords = ws.find_coords("X")
    return sum(ws.count_word_at("XMAS", coord) for coord in start_coords)


def part2(data: str) -> int:
    ws = Wordsearch(data)
    center_coords = ws.find_coords("A")
    return sum(ws.is_crossmas_at(coord) for coord in center_coords)
