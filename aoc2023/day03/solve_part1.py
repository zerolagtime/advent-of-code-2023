# pylint: disable=C0114,C0115,C0116

import logging
import re


logger = logging.getLogger(__name__)

class Grid:
    def __init__(self):
        self.symbols = ''
        self.width = None

    def extend(self, symbols):
        if not self.width:
            self.width = len(symbols)
        self.symbols += symbols

    def has_adjacent_symbol(self, start_pos: int, end_pos: int):
        neighbors = ''
        left_pos = start_pos - 1 if start_pos % self.width > 0 else start_pos
        right_border = False
        if end_pos % self.width > 0:
            right_pos = end_pos
        else:
            right_pos = end_pos - 1
            right_border = True

        # top row - above the grid is ok
        if left_pos >= self.width:
            if right_border:
                neighbors += self.symbols[(left_pos - self.width):(right_pos - self.width)]
            else:
                neighbors += self.symbols[(left_pos - self.width):(right_pos + 1 - self.width)]
        # left - start of the row is ok
        if start_pos != left_pos:
            neighbors += self.symbols[left_pos]
        # right - end of the row is okay
        if not right_border:  # right_pos is never in 0'th col
            neighbors += self.symbols[right_pos]
        # bottom - beyond the grid is ok
        if right_pos <= (len(self.symbols) - self.width):
            neighbors += self.symbols[(left_pos + self.width):(right_pos + self.width + 1)]
        leftovers = neighbors.replace('.', '')
        return len(leftovers) > 0

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
        if grid.has_adjacent_symbol(match.start(), match.end()):
            logger.debug('"%s" [%d:%d] has a neighbor symbol',
                         match.group(),match.start(),match.end())
            answer += int(match.group())
        else:
            logger.debug('"%s" [%d:%d] DOES NOT HAVE a neighbor symbol',
                         match.group(),match.start(),match.end())
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(main("project/day03/input.txt"))
