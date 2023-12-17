# pylint: disable=C0114,C0115,C0116

import unittest
import logging
import os
from tempfile import TemporaryDirectory
from textwrap import dedent

from aoc2023.day03 import solve_part1, solve_part2


logger = logging.getLogger()


# pylint: disable=C0114,C0115,C0116


class TestDay03(unittest.TestCase):

    def test_day03a_grid_import(self):
        grid = solve_part1.Grid()
        grid.extend('123')
        self.assertEqual(grid.symbols, '123')
        grid.extend('456')
        self.assertEqual(grid.symbols, '123456')

    def test_day03a_finditer(self):
        grid = solve_part1.Grid()
        grid.extend('467..114..')
        matches = list(grid.finditer())
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].group(), "467")
        self.assertEqual(matches[1].group(), "114")

    def test_day03a_neighbors1(self):  # C0114
        grid = solve_part1.Grid()
        grid.extend('467...114*.')
        matches = list(grid.finditer())
        self.assertFalse(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))
        self.assertTrue(grid.has_adjacent_symbol(matches[1].start(), matches[1].end()))

    def test_day03a_neighbors2a(self):
        grid = solve_part1.Grid()
        grid.extend('...13')
        matches = list(grid.finditer())
        self.assertFalse(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))
        grid.extend('..*..')
        matches = list(grid.finditer())
        self.assertTrue(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))

    def test_day03a_neighbors3(self):
        grid = solve_part1.Grid()
        grid.extend('...13.')
        matches = list(grid.finditer())
        self.assertFalse(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))
        grid.extend('.....*')
        matches = list(grid.finditer())
        self.assertTrue(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))

    def test_day03a_neighbors4(self):
        grid = solve_part1.Grid()
        grid.extend('10*13.')
        matches = list(grid.finditer())
        self.assertTrue(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))

    def test_day03a_neighbors5(self):
        grid = solve_part1.Grid()
        grid.extend('10#..')
        matches = list(grid.finditer())
        self.assertTrue(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))

    def test_day03a_neighbors6(self):
        grid = solve_part1.Grid()
        grid.extend('.....*')
        grid.extend('...13.')
        matches = list(grid.finditer())
        self.assertTrue(grid.has_adjacent_symbol(matches[0].start(), matches[0].end()))

    def test_day03a(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                        467..114..
                        ...*......
                        ..35..633.
                        ......#...
                        617*......
                        .....+.58.
                        ..592.....
                        ......755.
                        ...$.*....
                        .664.598..
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 4361)
        self.assertEqual(solve_part1.main('aoc2023/day03/input.txt'), 533784)

    def test_day03b_neighbors1(self):  # C0114
        grid = solve_part2.Grid()
        grid.extend('467...114*.')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[1].start(), matches[1].end())
        self.assertIn(('*', 9), neighbors)

    def test_day03b_neighbors2(self):
        grid = solve_part2.Grid()
        grid.extend('...13')
        grid.extend('..*..')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('*', 7), neighbors)

    def test_day03b_neighbors3(self):
        grid = solve_part2.Grid()
        grid.extend('...13.')
        grid.extend('.....*')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('*', 11), neighbors)

    def test_day03b_neighbors4(self):
        grid = solve_part2.Grid()
        grid.extend('10*13.')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('*', 2), neighbors)

    def test_day03b_neighbors5(self):
        grid = solve_part2.Grid()
        grid.extend('10#..')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('#', 2), neighbors)

    def test_day03b_neighbors6(self):
        grid = solve_part2.Grid()
        grid.extend('.....*')
        grid.extend('...13.')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('*', 5), neighbors)

    def test_day03b_neighbors7(self):
        grid = solve_part2.Grid()
        grid.extend('....*')
        grid.extend('...13')
        matches = list(grid.finditer())
        neighbors = grid.get_adjacent_symbols(matches[0].start(), matches[0].end())
        self.assertIn(('*', 4), neighbors)

    def test_day03b(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                        467..114..
                        ...*......
                        ..35..633.
                        ......#...
                        617*......
                        .....+.58.
                        ..592.....
                        ......755.
                        ...$.*....
                        .664.598..
                     ''').strip())
            self.assertEqual(solve_part2.main(tf), 467835)
        # self.assertEqual(solve_part2.main('project/day02/input.txt'), 54708)

    def test_day03bb(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t", encoding="utf8") as f:
                f.write(dedent('''
                        12.......*..
                        +.........34
                        .......-12..
                        ..78........
                        ..*....60...
                        78.........9
                        .5.....23..$
                        8...90*12...
                        ............
                        2.2......12.
                        .*.........*
                        1.1..503+.56
                     ''').strip())
            self.assertEqual(solve_part2.main(tf), 10195)
        self.assertEqual(solve_part2.main('aoc2023/day03/input.txt'), 78826761)
