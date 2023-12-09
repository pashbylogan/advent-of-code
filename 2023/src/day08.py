from typing import Dict, Tuple, TextIO
from math import gcd

def p1(file):
    answer = 0
    lines = file.readlines()
    instructions = lines.pop(0).strip()
    node_map = {}

    for line in lines[1:]:
        start, step = line.split(' = ')
        left, right = step.strip().replace('(', '').replace(')', '').split(', ')
        node_map[start] = (left, right)

    cur_node = 'AAA'
    while cur_node != 'ZZZ':
        if instructions[answer % len(instructions)] == 'R':
            cur_node = node_map[cur_node][1]
        else:
            cur_node = node_map[cur_node][0]
        answer += 1

    return answer


def p2(file: TextIO) -> int:
    answer: int = 0
    lines: list[str] = file.readlines()
    instructions: str = lines.pop(0).strip()
    node_map: Dict[str, Tuple[str, str]] = {}

    for line in lines[1:]:
        start, step = line.split(' = ')
        left, right = step.strip().replace('(', '').replace(')', '').split(', ')
        node_map[start] = (left, right)

    starting_nodes: list[str] = [key for key in node_map.keys() if key[-1] == 'A']
    cycle_lengths = [0] * len(starting_nodes)

    for i, cur_node in enumerate(starting_nodes):
        while cur_node[-1] != 'Z':
            if instructions[answer % len(instructions)] == 'R':
                cur_node = node_map[cur_node][1]
            else:
                cur_node = node_map[cur_node][0]
            cycle_lengths[i] += 1
            answer += 1

    lcm = cycle_lengths[0]
    for i in cycle_lengths[1:]:
        lcm = lcm * i // gcd(lcm, i)

    return lcm


with open('inputs/d8') as file:
    # print(p1(file))
    print(p2(file))
