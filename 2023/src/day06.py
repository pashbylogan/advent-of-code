import re, math

def p1(file):
    answer = []
    times = []
    distances = []

    for line in file:
        if 'Time' in line:
            times.extend([int(x) for x in re.findall(r'\d+', line)])
        if 'Distance' in line:
            distances.extend([int(x) for x in re.findall(r'\d+', line)])

    num_success = 0
    for time, distance in zip(times, distances):
        for i in range(time):
            num_success += 1 if (i * (time-i)) > distance else 0

        answer.append(num_success)
        num_success = 0

    return math.prod(answer)


def p2(file):
    num_success = 0
    time, distance = 0, 0

    for line in file:
        if 'Time' in line:
            time = int(''.join(re.findall(r'\d+', line)))
        if 'Distance' in line:
            distance = int(''.join(re.findall(r'\d+', line)))

    for i in range(time):
        num_success += 1 if (i * (time-i)) > distance else 0

    return num_success


with open('inputs/d6') as file:
    # print(p1(file))
    print(p2(file))
