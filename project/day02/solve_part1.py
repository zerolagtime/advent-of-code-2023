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
    logger.debug(f'  {"   -   ".join(games)}')
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
    total_colors = {'red': 0, 'green': 0, 'blue': 0}
    for round in stats['rounds']:
        for k, v in round.items():
            if v > max_colors[k]:
                return True
    return False
    for color, total in total_colors.items():
        if max_colors[color] < total:
            logging.debug(f'Game {stats["num"]} is invalid because there are {total} {color} cubes (max {max_colors[color]})')
            return True
    logger.debug(f'Game {stats["num"]} is a valid game')
    return False

def main(source_file):
    answer = 0
    with open(source_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            stats = game_parse(line)
            if not is_invalid(stats):
                logger.debug(f'    VAlID: {line}')
                answer += stats['num']
            else:
                logger.debug(f'NOT VALID: {line}')
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(main("project/day02/input.txt"))
