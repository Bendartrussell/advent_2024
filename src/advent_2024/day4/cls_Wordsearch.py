from typing import NamedTuple, Self


class Coord(NamedTuple):
    x: int
    y: int


    def __add__(self, other) -> Self:
        if not isinstance(other, Coord):
            return NotImplemented
        else:
            return self.__class__(self.x + other.x, self.y + other.y)


DIRECTIONS = (
    Coord(1, 0),
    Coord(1, 1),
    Coord(0, 1),
    Coord(-1, 1),
    Coord(-1, 0),
    Coord(-1, -1),
    Coord(0, -1),
    Coord(1, -1),
)


class Wordsearch:
    def __init__(self, data: str):
        self.table = [list(line) for line in data.strip().split("\n")]
        self.height = len(self.table)
        self.width = len(self.table[0])
    

    def at(self, coord: Coord) -> str:
        return self.table[coord.y][coord.x]


    def is_in_range(self, coord: Coord) -> bool:
        return (0 <= coord.x < self.width) and (0 <= coord.y < self.height)
    
    
    def find_coords(self, letter: str) -> list[Coord]:
        match_coords: list[Coord] = []

        for y, row in enumerate(self.table):
            for x, elem in enumerate(row):
                if elem == letter:
                    match_coords.append(Coord(x, y))
        
        return match_coords


    def count_word_at(self, word: str, coord: Coord) -> int:
        count = 0

        for i in range(8):
            search_dir = DIRECTIONS[i]
            cursor = coord + search_dir

            for i in range(1, len(word)):
                if not self.is_in_range(cursor):
                    break

                if word[i] == self.at(cursor):
                    cursor += search_dir
                else:
                    break
            else:
                count += 1
        
        return count
