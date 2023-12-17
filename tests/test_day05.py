# pylint: disable=C0114,C0115,C0116

import unittest
import logging
import os
from tempfile import TemporaryDirectory
from textwrap import dedent

from aoc2023.day04 import solve_part1, solve_part2


logger = logging.getLogger()


# pylint: disable=C0114,C0115,C0116


class TestDay05(unittest.TestCase):
    @unittest.skip('not ready')
    def test_day05a(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 4361)
        self.assertEqual(solve_part1.main('aoc2023/day05/input.txt'), 533784)

    @unittest.skip('not ready')
    def test_day05b(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 4361)
        self.assertEqual(solve_part1.main('aoc2023/day05/input.txt'), 533784)
