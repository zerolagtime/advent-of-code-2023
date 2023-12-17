# pylint: disable=C0114,C0115,C0116

import logging
import re

logger = logging.getLogger(__name__)

class Grid:
    def __init__(self):
        self.symbols = ''
        self.width = None
        self.gear_half_pos = [] # a tuple (pos, int)

    def extend(self, symbols):
        if not self.width:
            self.width = len(symbols)
        self.symbols += symbols

    def get_adjacent_symbols(self, start_pos: int, end_pos: int) -> list:
        neighbors = ''
        left_pos = start_pos - 1 if start_pos % self.width > 0 else start_pos
        right_border = False
        if end_pos % self.width > 0:
            right_pos = end_pos
        else:
            right_pos = end_pos - 1
            right_border = True

        neighbor_pos = []
        # top row - above the grid is ok
        if left_pos >= self.width:
            neighbors += self.symbols[(left_pos - self.width):(right_pos + 1 - self.width)]
            neighbor_pos.extend(list(range((left_pos - self.width),
                                            (right_pos + 1 - self.width))))
        # left - start of the row is ok
        if start_pos != left_pos:
            neighbors += self.symbols[left_pos]
            neighbor_pos.append(left_pos)
        # right - end of the row is okay
        if not right_border:  # right_pos is never in 0'th col
            neighbors += self.symbols[right_pos]
            neighbor_pos.append(right_pos)
        # bottom - beyond the grid is ok
        if right_pos <= (len(self.symbols) - self.width):
            neighbors += self.symbols[(left_pos + self.width):(right_pos + self.width + 1)]
            neighbor_pos.extend(list(range((left_pos + self.width),
                                           (right_pos + self.width + 1)+1)))
        neighbor_tuple_list = [(neighbors[x], neighbor_pos[x]) for x in range(len(neighbors))]
        return neighbor_tuple_list

    def find_adjacent_gear(self, start_pos, end_pos):
        neighbors = self.get_adjacent_symbols(start_pos, end_pos)
        this_number = int(self.symbols[start_pos:end_pos])
        for symbol,pos in neighbors:
            if symbol == '*':
                logger.info('  Found gear %d at %d. Adding it to the list.',
                             this_number, pos)
                self.gear_half_pos.append((pos, this_number, start_pos))

    def finditer(self, pattern=r'\b(\d+)(?!\*)?\b'):
        for match in re.finditer(pattern, self.symbols):
            yield match

    @staticmethod
    def sort_gears(gear1: tuple, gear2: tuple) -> tuple:
        if gear1[0] > gear2[0]:
            return gear2, gear1
        if gear1[0] == gear2[0] and gear1[1] > gear2[1]:
            return gear2, gear1
        if gear1[0] == gear2[0] and gear1[1] == gear2[1] and gear1[2] > gear2[2]:
            return gear2, gear1
        return gear1, gear2

    def get_adjacent_gears(self):
        gear_pairs = set()
        for half in self.gear_half_pos:
            for other_half in self.gear_half_pos:
                if other_half != half and half[0] == other_half[0]:
                    pair = Grid.sort_gears(half, other_half)
                    gear_pairs.add(pair)
        for pair in gear_pairs:
            yield pair[0][1], pair[1][1]

def main(source_file):
    answer = 0
    grid = Grid()
    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            grid.extend(line)
    for match in grid.finditer(r'\b(\d+)\b'):
        grid.find_adjacent_gear(match.start(), match.end())
    for left, right in grid.get_adjacent_gears():
        logger.info('Matched gear %d with %d', left, right)
        answer += left * right
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(main("project/day03/input.txt"))
