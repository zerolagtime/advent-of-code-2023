import logging
import re

logger = logging.getLogger(__name__)

def main(source_file):
    sum = 0
    # we need to match the first occurrence of any word,
    # not just blind substitution
    pattern_first = r'(one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0)' 
    pattern_last = r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0))' 
    replace_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'zero': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, 
    }
    with open(source_file, "r") as f:
        for line in f:
            line = line.strip()
            first = re.search(pattern_first, line).group()
            last = re.findall(pattern_last, line)[-1]
            to_add = replace_dict[first]*10 + replace_dict[last]
            sum += to_add
            logger.debug(f'translate {line} => ({first},{last})=> {to_add}')
    logger.info(f'returned sum {sum}')
    return sum

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(main("project/day01/input.txt"))
