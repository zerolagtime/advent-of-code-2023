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
            if right_border:
                neighbors += self.symbols[(left_pos - self.width):(right_pos - self.width)]
                neighbor_pos.extend(list(range((left_pos - self.width),
                                               (right_pos - self.width) + 1)))
            else:
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


    def _get_previous_gear(self, gear_pos, gear_size):
        other_gear_size = None
        for pos, other_gear in self.gear_half_pos:
            if pos == gear_pos:
                other_gear_size = other_gear
        self.gear_half_pos.append((gear_pos, gear_size))
        return other_gear_size


    def get_adjacent_gear(self, start_pos, end_pos):
        neighbors = self.get_adjacent_symbols(start_pos, end_pos)
        this_number = int(self.symbols[start_pos:end_pos])
        adjacent_gear = None
        for symbol,pos in neighbors:
            if symbol == '*':
                logger.info('  Found gear %d at %d. Adding it to the list.',
                             this_number, pos)
                adjacent = self._get_previous_gear(pos, this_number)
                if adjacent and not adjacent_gear:
                    adjacent_gear = adjacent
        return adjacent_gear

    def finditer(self, pattern=r'\b(\d+)(?!\*)?\b'):
        for match in re.finditer(pattern, self.symbols):
            yield match

def main(source_file):
    answer = 0
    with open(source_file, "r", encoding="utf-8") as f:
        grid = Grid()
        for line in f:
            line = line.rstrip("\n")
            grid.extend(line)
    for match in grid.finditer(r'\b(\d+)\b'):
        this_gear_size = int(match.group())
        other_gear_size = grid.get_adjacent_gear(match.start(), match.end())
        if other_gear_size:
            logger.info('Matched gear %d with %d', this_gear_size,
                         other_gear_size)
            answer += this_gear_size * other_gear_size
        else:
            logger.debug('No match for gear %d.', this_gear_size)
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(main("project/day03/input.txt"))
