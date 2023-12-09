from typing import Dict, Tuple, TextIO

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

    cur_nodes: list[str] = [key for key in node_map.keys() if key[-1] == 'A']
    while True:
        print(answer, cur_nodes)
        if instructions[answer % len(instructions)] == 'R':
            cur_nodes = [node_map[cur_node][1] for cur_node in cur_nodes]
        else:
            cur_nodes = [node_map[cur_node][0] for cur_node in cur_nodes]

        answer += 1

        if all([cur_node[-1] == 'Z' for cur_node in cur_nodes]):
            break

        if answer > 10:
            break

    return answer


with open('inputs/d8') as file:
    # print(p1(file))
    print(p2(file))
