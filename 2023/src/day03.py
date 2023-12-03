import re, string

def _get_element(x, y, surrounding_lines):
    if x < 0 or x >= len(surrounding_lines) or y < 0 or y >= len(surrounding_lines[0]):
        return '.'
    else:
        return surrounding_lines[x][y]

def _check_for_symbols(line_num, file_lines, match):
    directions = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, 1], [0, -1]]
    symbols = set(string.punctuation + string.whitespace) - {'.', '\n'}

    starting_line = max(line_num-1, 0)
    ending_line = min(line_num+2, len(file_lines))
    surrounding_lines = file_lines[starting_line:ending_line]

    
    if not starting_line:
        match_line = 0
    else:
        match_line = 1

    start, end = match

    num = file_lines[line_num][start:end] # TODO: Remove

    for i in range(start, end):
        for d1, d2 in directions:
            # print(_get_element(match_line + d1, i + d2, surrounding_lines))
            if num == '122':
                print(match_line + d1, i + d2, _get_element(match_line + d1, i + d2, surrounding_lines))

            if _get_element(match_line + d1, i + d2, surrounding_lines) in symbols:
                return True

    return False


def p1(file):
    sum = 0
    lines = file.readlines()

    for i, line in enumerate(lines):
        if i > 3:
            continue

        matches = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        for m in matches:
            if _check_for_symbols(i, lines, m):
                sum += int(line[m[0]:m[1]])

    return sum


def p2(file):
    return 0


with open('inputs/d3') as file:
    print(p1(file))
    # print(p2)
