def p1(file):
    lines = file.readlines()
    return _calculate_north_load(lines)


def _calculate_north_load(lines):
    answer = 0
    num_rows = len(lines)
    lines = list(map(list, zip(*lines)))

    for l in lines:
        current_stop = 0
        num_os = 0
        for j, c in enumerate(l):
            if c == '#':
                current_stop = j + 1
                num_os = 0
            elif c == 'O':
                answer += num_rows - current_stop - num_os
                num_os += 1

    return answer


def p2(file):
    lines = file.readlines()
    
    # Get the state of lines after 1000000000 cycles
    return _calculate_north_load(lines)


# Filenames will always be in the format dXX.py
day = f"d{__file__.split('/')[-1].split('.')[0].replace('day', '')}"
with open(f'inputs/{day}') as file:
    print(p1(file))
    # print(p2(file))
