import unittest
import logging
import os
from tempfile import TemporaryDirectory
from textwrap import dedent

logging.basicConfig(level=logging.DEBUG)

from project.day02 import solve_part1, solve_part2

class TestDay02(unittest.TestCase):

    def test_day02a_game_parse(self):
        source = 'Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red; 10 green, 1 red, 2 blue; 2 blue, 3 red'
        expect = {'num': 1, 'rounds': [
            {'red': 0, 'green': 8, 'blue': 0},
            {'red': 1, 'green': 5, 'blue': 6},
            {'red': 4, 'green': 2, 'blue': 1},
            {'red': 1, 'green': 10, 'blue': 2},
            {'red': 3, 'green': 0, 'blue': 2},
        ]}
        self.assertEqual(solve_part1.game_parse(source), expect)
        tests = {
            'Game 100: 1 green': {'num': 100, 'rounds': [{'red': 0, 'green': 1, 'blue': 0}]},
            'Game 99: 1 red': {'num': 99, 'rounds': [{'red': 1, 'green': 0, 'blue': 0}]},
            'Game 98: 1 green': {'num': 98, 'rounds': [{'red': 0, 'green': 1, 'blue': 0}]},
            'Game 97: 1 blue': {'num': 97, 'rounds': [{'red': 0, 'green': 0, 'blue': 1}]},
            'Game 96: 1 red, 2 blue': {'num': 96, 'rounds': [{'red': 1, 'green': 0, 'blue': 2}]},
            'Game 95: 2 blue, 1 red': {'num': 95, 'rounds': [{'red': 1, 'green': 0, 'blue': 2}]},
            'Game 94: 1 green, 2 red': {'num': 94, 'rounds': [{'red': 2, 'green': 1, 'blue': 0}]},
            'Game 93: 2 red, 1 green': {'num': 93, 'rounds': [{'red': 2, 'green': 1, 'blue': 0}]},
        }
        for t,e in tests.items():
            self.assertEqual(solve_part1.game_parse(t), e)

    def test_day02a_is_invalid(self):
        source = 'Game 1: 8 green; 5 green, 6 blue, 1 red; 2 green, 1 blue, 4 red; 10 green, 1 red, 2 blue; 2 blue, 3 red'
        stat = solve_part1.game_parse(source)
        self.assertTrue(solve_part1.is_invalid)

    def test_day02a(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t") as f:
                f.write(dedent('''
                    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
                    ''').strip())
            self.assertEqual(solve_part1.main(tf), 8)
        self.assertEqual(solve_part1.main('project/day02/input.txt'), 2149)

    def test_day02b(self):
        with TemporaryDirectory() as td:
            tf = os.path.join(td,"temp1")
            with open(tf, "w+t") as f:
                f.write(dedent('''
                    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
                    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
                    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
                    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
                    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
                    ''').strip())
            self.assertEqual(solve_part2.main(tf), 2286)
        # self.assertEqual(solve_part2.main('project/day02/input.txt'), 54708)
