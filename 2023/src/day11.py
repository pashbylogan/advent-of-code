import re

def p1(file):
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
        grid.insert(i, grid[i])

    for i in vertical_lines[::-1]:
        grid = [l[:i] + l[i] + l[i:] for l in grid]

    # Get pairs of coordinates
    galaxies = []
    for i, l in enumerate(grid):
        for m in re.finditer(r'#', l):
            galaxies.append((i, m.start()))

    galaxy_pairs = []
    for i, galaxy in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            galaxy_pairs.append((galaxy, galaxies[j]))

    return sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in galaxy_pairs])


def p2(file):
    grid = [l.strip() for l in file]

    horizontal_lines = []
    for i, horizontal_line in enumerate(grid):
        if all([c == '.' for c in horizontal_line]):
            horizontal_lines.append(i)

    vertical_lines = []
    for i, vertical_line in enumerate(zip(*grid)):
        if all([c == '.' for c in vertical_line]):
            vertical_lines.append(i)

    # Get pairs of coordinates
    galaxies = []
    for i, l in enumerate(grid):
        for m in re.finditer(r'#', l):
            h_idx = i
            v_idx = m.start()

            for idx in horizontal_lines:
                if idx < i:
                    h_idx += 999999

            for idx in vertical_lines:
                if idx < m.start():
                    v_idx += 999999

            galaxies.append((h_idx, v_idx))

    galaxy_pairs = []
    for i, galaxy in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            galaxy_pairs.append((galaxy, galaxies[j]))

    return sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in galaxy_pairs])


# Filenames will always be in the format dXX.py
day = f"d{__file__.split('/')[-1].split('.')[0].replace('day', '')}"
with open(f'inputs/{day}') as file:
    # print(p1(file))
    print(p2(file))
