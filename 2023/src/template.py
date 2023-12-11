def p1(file):
    answer = 0
    for line in file:
        ...
    return answer


def p2(file):
    answer = 0
    for line in file:
        ...
    return answer


# Filenames will always be in the format dXX.py
day = f"d{__file__.split('/')[-1].split('.')[0].replace('day', '')}"
with open(f'inputs/d{day}') as file:
    print(p1(file))
    # print(p2(file))
