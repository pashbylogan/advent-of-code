import re

def part_1(i, line):
    game_id = int(line.split(':')[0].split()[1])

    max_cubes = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for color in max_cubes.keys():
        pattern = r'\d+\s+' + re.escape(color)
        matches = re.findall(pattern, line)

        for match in matches:
            num, color = match.split()

            max_cubes[color] = int(num) if int(num) > max_cubes[color] else max_cubes[color]

    if max_cubes['red'] > 12 or max_cubes['blue'] > 14 or max_cubes['green'] > 13:
        return 0
    else:
        return game_id


def part_2(i, line):
    max_cubes = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for color in max_cubes.keys():
        pattern = r'\d+\s+' + re.escape(color)
        matches = re.findall(pattern, line)

        for match in matches:
            num, color = match.split()

            max_cubes[color] = int(num) if int(num) > max_cubes[color] else max_cubes[color]

    return max_cubes['red'] * max_cubes['blue'] * max_cubes['green']


with open('inputs/day02.txt') as file:
    sum = 0

    for i, line in enumerate(file):
        sum += part_2(i, line)

    print(sum)
