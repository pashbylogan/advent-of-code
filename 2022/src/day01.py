def get_elf_inventory(lines):
    elf_inventories = [0]

    elf_num = 0
    for i in range(len(lines)):
        if lines[i] == '':
            elf_num += 1
            elf_inventories.append(0)
            continue

        elf_inventories[elf_num] += int(lines[i])

    return elf_inventories

def part1(lines):
    elf_inventories = get_elf_inventory(lines)

    return max(elf_inventories)

def part2(lines):
    elf_inventories = get_elf_inventory(lines)
    
    sum_of_three_elfs = 0
    for i in range(3):
        sum_of_three_elfs += elf_inventories.pop(elf_inventories.index(max(elf_inventories))) if elf_inventories else 0

    return sum_of_three_elfs



def main():
    filename = '../inputs/day01.txt'

    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    # print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main()
