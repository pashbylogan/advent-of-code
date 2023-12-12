import re

def _find_first_possible_location(springs: str, num_broken: int):
    matches = [(match.group(), match.start()) for match in re.finditer(r'([#]+|[?]+)', springs)]

    for m, m_idx in matches:
        if all([c == '#' for c in m]) and len(m) >= num_broken:
            # print(springs, num_broken, m_idx)
            return m_idx

        l = 0
        r = num_broken

        while l + r <= len(m):
            if (l == 0 or m[l-1] == '?') and (l + r == len(m) or m[l + r] == '?'):
                # print(springs, num_broken, m_idx + l)
                return m_idx + l
            
            l += 1

    # print('couldnt find match', springs, num_broken)
    return -1


def _recurse_springs(springs: str, arrangement: list[int]):
    if not arrangement:
        # print(springs, arrangement, 1)
        return 1

    output = 0

    first_location_idx = _find_first_possible_location(springs, arrangement[0])
    # print('\nsprings', springs)
    # print('arrangement first num', arrangement[0])
    # print('first_location', first_location_idx)
    if first_location_idx == -1:
        # print(springs, arrangement, 1)
        return 0

    # Case 1
    changed_string = list(springs)
    changed_string[first_location_idx] = '.'
    changed_string= ''.join(changed_string)
    output += _recurse_springs(changed_string, arrangement)

    # Case 2
    changed_string = list(springs)
    for i in range(first_location_idx, first_location_idx + arrangement[0]):
        changed_string[i] = '#'
    changed_string= ''.join(changed_string)
    # print(springs, arrangement, _recurse_springs(changed_string, arrangement[1:]))
    output += _recurse_springs(changed_string, arrangement[1:])

    # print(springs, arrangement, output)
    return output
    


def p1(file):
    answer = 0
    for i, line in enumerate(file):
        if i != 1:
            continue

        print(line)
        springs, damaged_groups = line.strip().split()
        damaged_groups = [int(n) for n in damaged_groups.split(',')]

        answer += _recurse_springs(springs, damaged_groups)

    return answer


def p2(file):
    answer = 0
    for line in file:
        ...
    return answer


# Filenames will always be in the format dXX.py
day = f"d{__file__.split('/')[-1].split('.')[0].replace('day', '')}"
with open(f'inputs/{day}_example') as file:
    print(p1(file))
    # print(p2(file))
