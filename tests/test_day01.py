import unittest
import logging
import os
from tempfile import TemporaryDirectory
from textwrap import dedent

logging.basicConfig(level=logging.DEBUG)

from aoc2023.day01 import solve_part1, solve_part2

class TestDay01(unittest.TestCase):
    def test_day01a(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t") as f:
                f.write(dedent('''
                    1abc2
                    pqr3stu8vwx
                    a1b2c3d4e5f
                    treb7uchet  
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 142)
        self.assertEqual(solve_part1.main('aoc2023/day01/input.txt'), 54708)


    def test_day01b(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t") as f:
                f.write(dedent('''
                    oneight
                    two1nine
                    eightwothree
                    abcone2threexyz
                    xtwone3four
                    4nineeightseven2
                    zoneight234
                    7pqrstsixteen
                    ''').strip())
            self.assertEqual(solve_part2.main(tf), 299)
        self.assertEqual(solve_part2.main('aoc2023/day01/input.txt'), 54087)