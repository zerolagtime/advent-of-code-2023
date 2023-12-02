import unittest

from project.day01 import solve_part1

class TestDay01(unittest.TestCase):
    def test_day01(self):
        self.assertEqual(solve_part1.main('project/day01/input.txt'), 54708)