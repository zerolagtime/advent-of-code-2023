import logging
import re

logger = logging.getLogger(__name__)


def main(source_file):
    answer = 0
    with open(source_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
    return answer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(main("project/day03/input.txt"))