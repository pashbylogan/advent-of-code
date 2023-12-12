from collections import deque

directions_map = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(0, 1), (-1, 0)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)]
}

def _visualize_graph_with_distances(graph, queue):
    nodes = [node[0] for node in queue]
    distances = [node[1] for node in queue]

    for i, line in enumerate(graph):
        for j, char in enumerate(line):
            if (i, j) in nodes:
                print(distances[nodes.index((i, j))], end='')
            else:
                print(char, end='')
        print()
    print()


def _find_s_neighbors(graph, s):
    valid_pipes = {
        (1, 0): ['|', 'L', 'J'],
        (-1, 0): ['|', '7', 'F'],
        (0, 1): ['-', 'J', '7'],
        (0, -1): ['-', 'L', 'F'],
    }

    neighbors = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x = s[0] + d[0]
        y = s[1] + d[1]

        if 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] in valid_pipes[d]:
            # if graph[x][y] != '#':
            neighbors.append((x, y)) 

    assert len(neighbors) <= 2
    return neighbors


def _get_neighbors(graph, vertex):
    neighbors = []
    direction = directions_map[graph[vertex[0]][vertex[1]]]

    for d in direction:
        x = vertex[0] + d[0]
        y = vertex[1] + d[1]

        if 0 <= x < len(graph) and 0 <= y < len(graph[0]):
            neighbors.append((x, y)) 

    assert len(neighbors) <= 2
    return neighbors


def _bfs(graph, start):
    queue = deque([(start, 0)])
    visited = set()
    longest_path = 0

    while queue:
        vertex, distance = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)
        longest_path = max(longest_path, distance)

        if graph[vertex[0]][vertex[1]] == 'S':
            for neighbor in _find_s_neighbors(graph, vertex):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
        else:
            for neighbor in _get_neighbors(graph, vertex):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

        # _visualize_graph_with_distances(graph, queue)

    return longest_path


def p1(file):
    lines = [line.strip() for line in file]

    starting_node = (0, 0)
    for i, l in enumerate(lines):
        if 'S' in l:
            starting_node = (i, l.index('S'))

    return _bfs(lines, starting_node)


def _bfs_p2(graph, start):
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        vertex, distance = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)

        if graph[vertex[0]][vertex[1]] == 'S':
            for neighbor in _find_s_neighbors(graph, vertex):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
        else:
            for neighbor in _get_neighbors(graph, vertex):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

        # _visualize_graph_with_distances(graph, queue)

    return visited


def p2(file):
    lines = [line.strip() for line in file]

    starting_node = (0, 0)
    for i, l in enumerate(lines):
        if 'S' in l:
            starting_node = (i, l.index('S'))

    perimeter = _bfs_p2(lines, starting_node)
    print(perimeter)

    return len(perimeter)

day = f"d{__file__.split('/')[-1].split('.')[0].replace('day', '')}"
with open(f'inputs/{day}_example') as file:
    # print(p1(file))
    print(p2(file))
