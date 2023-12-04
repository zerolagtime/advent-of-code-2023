import logging
import os
import re
from math import prod

logger = logging.getLogger(__name__)

def game_parse(line) -> dict:
    game_total = { 'num': None,
                   'rounds': [
                   ]
                 }
    matches = re.search(r'^Game\s+(\d+):\s*(.*)$', line)
    game_total['num'] = int(matches.group(1))
    results = matches.group(2)
    games = results.split(';')
    logger.debug(f'  {"   -   ".join(games)}')
    for game in games:
        grab = [ x.strip() for x in game.split(',')]
        all_colors = {'red': 0, 'blue': 0, 'green': 0}
        for color_count in grab:
            count, color = color_count.split(' ')
            all_colors[color] = int(count)
        game_total['rounds'].append(all_colors)
    return game_total

def game_power(stats) -> dict:
    maxes = {'red': 0, 'green': 0, 'blue': 0}
    for round in stats['rounds']:
        for color in maxes:
            maxes[color] = max(maxes[color], round[color])
    return prod(maxes.values())

def main(source_file):
    answer = 0
    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            stats = game_parse(line)
            power = game_power(stats)
            answer += power
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(main("project/day02/input.txt"))
