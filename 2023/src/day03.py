import re, string, math

def _get_element(x, y, surrounding_lines):
    if x < 0 or x >= len(surrounding_lines) or y < 0 or y >= len(surrounding_lines[0]):
        return '.'
    else:
        return surrounding_lines[x][y]

def _check_for_symbols(line_num, file_lines, match):
    directions = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, 1], [0, -1]]
    symbols = set(string.punctuation + string.whitespace) - {'.', '\n'}
    start, end = match

    for i in range(start, end):
        for d1, d2 in directions:
            if _get_element(line_num + d1, i + d2, file_lines) in symbols:
                return True

    return False


def p1(file):
    sum = 0
    lines = file.readlines()

    for i, line in enumerate(lines):
        matches = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for m in matches:
            if _check_for_symbols(i, lines, m):
                sum += int(line[m[0]:m[1]])

    return sum

def _check_for_symbols_p2(gears, line_num, file_lines, match):
    directions = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, 1], [0, -1]]
    symbols = {'*'}
    start, end = match

    for i in range(start, end):
        for d1, d2 in directions:
            if _get_element(line_num + d1, i + d2, file_lines) in symbols:
                key = str(line_num + d1) + str(i + d2)
                num = file_lines[line_num][start:end]

                if key in gears:
                    gears[key].add(num)
                else:
                    gears[key] = {num}

                continue


def p2(file):
    gears = {}
    lines = file.readlines()

    for i, line in enumerate(lines):
        matches = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for m in matches:
            _check_for_symbols_p2(gears, i, lines, m)

    s = 0
    for _, gear in gears.items():
        if len(gear) == 2:
            s += math.prod([int(num) for num in gear])

    return s

with open('inputs/d3') as file:
    # print(p1(file))
    print(p2(file))
