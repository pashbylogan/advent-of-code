def p1(file):
    answer = 0
    grid = [l.strip() for l in file]

    horizontal_lines = []
    for i, horizontal_line in enumerate(grid):
        if all([c == '.' for c in horizontal_line]):
            horizontal_lines.append(i)

    vertical_lines = []
    for i, vertical_line in enumerate(zip(*grid)):
        if all([c == '.' for c in vertical_line]):
            vertical_lines.append(i)

    # Expand grid
    for i in horizontal_lines[::-1]:
        grid.append(grid[i])

    for i in vertical_lines[::-1]:
        for j, line in enumerate(grid):
            grid[j] += line[i]

    print('\n'.join(grid))

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
