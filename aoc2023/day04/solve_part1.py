# pylint: disable=C0114,C0115,C0116

import logging
import re

logger = logging.getLogger(__name__)

class Card():
    def __init__(self, line: str):
        self.card_number = None
        self.my_numbers = []
        self.winning_numbers = []
        self.score = 0
        self.parse_line(line)
        self._compute_score()
    
    def parse_line(self, line: str):
        self.card_number = int(line.split(":")[0].split(" ")[-1])
        my_str, winning_str = line.split(":")[1].split("|")[0:2]
        my_str, winning_str = my_str.rstrip(), winning_str.rstrip()
        self.my_numbers = [int(my_str[x:x+3].strip()) \
                           for x in range(0, len(my_str), 3) ]
        self.winning_numbers = [int(winning_str[x:x+3].strip()) \
                                for x in range(0, len(winning_str), 3) ]
    def _compute_score(self):
        intersection = set(self.my_numbers).intersection(set(self.winning_numbers))
        if intersection:
            self.score = 2 ** (len(intersection) - 1)

def main(source_file):
    answer = 0
    cards = []
    with open(source_file, "r") as f:
        for line in f:
            cards.append(Card(line.rstrip("\n")))
            answer += cards[-1].score
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(main("aoc2023/day04/input.txt"))
