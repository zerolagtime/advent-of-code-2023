def main(source_file):
    sum = 0

    translate_dict = str.maketrans('', '', 'abcdefghijklmnopqrstuvwxyz')
    with open(source_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            line = line.translate(translate_dict)
            if len(line) == 1:
                line = f'{line}{line}'
            sum += (int(line[0])*10 + int(line[-1]))

    return sum

if __name__ == '__main__':
    print(main("project/day01/input.txt"))
