'''
'''

def part1(lines):
    ...

def part2(lines):
    ...

def main():
    filename = '../inputs/day03.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    print(part1(lines))
    # print(part2(lines))

if __name__ == '__main__':
    main()
