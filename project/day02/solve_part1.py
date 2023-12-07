# pylint: disable=C0114,C0115,C0116

import logging
import re

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
    logger.debug('  %s', "   -   ".join(games))
    for game in games:
        grab = [ x.strip() for x in game.split(',')]
        all_colors = {'red': 0, 'blue': 0, 'green': 0}
        for color_count in grab:
            count, color = color_count.split(' ')
            all_colors[color] = int(count)
        game_total['rounds'].append(all_colors)
    return game_total

def is_invalid(stats: dict):
    max_colors = {'red': 12, 'green': 13, 'blue': 14}
    for one_round in stats['rounds']:
        for k, v in one_round.items():
            if v > max_colors[k]:
                return True
    return False


def main(source_file):
    answer = 0
    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            stats = game_parse(line)
            if not is_invalid(stats):
                logger.debug('    ValID: %s', line)
                answer += stats['num']
            else:
                logger.debug('NOT VALID: %s', line)
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(main("project/day02/input.txt"))
