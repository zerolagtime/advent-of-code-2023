# pylint: disable=C0114,C0115,C0116

import unittest
import logging
import os
from tempfile import TemporaryDirectory
from textwrap import dedent

from aoc2023.day04 import solve_part1, solve_part2


logger = logging.getLogger()


# pylint: disable=C0114,C0115,C0116


class TestDay04(unittest.TestCase):
    def test_parse_card(self):
        line = "Card   5: 41  8 |  8 13 "
        c = solve_part1.Card(line)
        self.assertEqual(c.card_number, 5)
        self.assertEqual(c.my_numbers, [41, 8])
        self.assertEqual(c.winning_numbers, [8, 13])
    
    def test_score_card(self):
        line = "Card   5: 41  8 |  8 13 "
        c = solve_part1.Card(line)
        self.assertEqual(c.score, 1)
        
    def test_day04a(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                    Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
                    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
                    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
                    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
                    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
                    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 13)
        self.assertEqual(solve_part1.main('aoc2023/day04/input.txt'), 23941)

    @unittest.skip('not ready')
    def test_day04b(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 4361)
        self.assertEqual(solve_part1.main('aoc2023/day04/input.txt'), 533784)
