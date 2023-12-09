import re

def p1(file):
    seed_map = {}

    for line in file:
        if 'seeds:' in line:
            matches = re.findall(r'\d+', line)

            for m in matches:
                seed_map[int(m)] = int(m)
        elif line[0].isdigit():
            nums = [int(n) for n in line.split()]
            for key in seed_map:
                if key in range(nums[1], nums[1] + nums[2]):
                    seed_map[key] = (key - nums[1]) + nums[0]
        elif not line.strip():
            seed_map = {v: v for _, v in seed_map.items()}
        else:
            continue

    return min(seed_map.values())


def p2(file):
    seeds = set()
    remove_set = set()
    add_set = set()
    has_mapping = set()
    cur_map = '' #TODO: Remove, only for testing
    total_seeds = 0 # TODO: Remove, only for testing

    for line in file:
        cur_map = line.split(' map:')[0] if 'map' in line else cur_map

        if 'seeds:' in line:
            matches = re.findall(r'\d+', line)

            for i in range(0, len(matches), 2):
                # (number at start of range, length of range)
                seeds.add((int(matches[i]), int(matches[i + 1])))
                total_seeds += int(matches[i+1])
        elif line[0].isdigit():
            nums = [int(n) for n in line.split()]
            mapping_start = nums[1]
            mapping_end = nums[1] + nums[2] - 1
            destination_start = nums[0]

            for seed_range in seeds:
                seed_start = seed_range[0]
                seed_end = seed_range[0] + seed_range[1] -1 

                # Mapping the beginning of seed range
                if mapping_start <= seed_start <= mapping_end and seed_end > mapping_end:
                    remove_set.add(seed_range)
                    add_set.add((destination_start, mapping_end - seed_start + 1))
                    has_mapping.add((seed_start, mapping_end - seed_start + 1))

                    if (mapping_end + 1, seed_range[1] - (mapping_end - seed_start + 1)) not in has_mapping:
                        add_set.add((mapping_end + 1, seed_range[1] - (mapping_end - seed_start + 1)))

                    if 'temperature-to' in cur_map:
                        print('testing case 1', seed_start, mapping_start, mapping_end, destination_start)
                        print((destination_start, mapping_end - seed_start + 1))
                        print((mapping_end + 1, seed_range[1] - (mapping_end - seed_start + 1)))

                # Mapping the end of the seed range
                elif seed_start < mapping_start and mapping_start <= seed_end <= mapping_end:
                    seed_mapping_diff = 1 + seed_end - mapping_start
                    remove_set.add(seed_range)
                    add_set.add((destination_start, seed_mapping_diff))
                    has_mapping.add((mapping_start, seed_mapping_diff))
                    
                    if (seed_start, seed_range[1] - seed_mapping_diff) not in has_mapping:
                        add_set.add((seed_start, seed_range[1] - seed_mapping_diff))
                    if 'temperature-to' in cur_map:
                        print('testing case 2', seed_start, mapping_start, mapping_end, destination_start)

                # Mapping the whole seed range
                elif mapping_start <= seed_start <= mapping_end and mapping_start <= seed_end <= mapping_end:
                    remove_set.add(seed_range)
                    add_set.add((destination_start + (seed_start - mapping_start), seed_range[1]))
                    has_mapping.add((seed_start, seed_range[1]))
                    if 'temperature-to' in cur_map:
                        print('testing case 3', seed_start, mapping_start, mapping_end, destination_start)

                # Mapping the middle of the seed range
                elif seed_start <= mapping_start <= seed_end and seed_start <= mapping_end <= seed_end:
                    remove_set.add(seed_range)
                    add_set.add((destination_start, nums[2]))
                    has_mapping.add((mapping_start, nums[2]))

                    if (seed_start, mapping_start - seed_start) not in has_mapping:
                        add_set.add((seed_start, mapping_start - seed_start))

                    if (seed_start + (mapping_start - seed_start) + nums[2], seed_range[1] - nums[2] - (mapping_start - seed_start)) not in has_mapping:
                        add_set.add((seed_start + (mapping_start - seed_start) + nums[2], seed_range[1] - nums[2] - (mapping_start - seed_start)))
                    if 'temperature-to' in cur_map:
                        print('testing case 4', seed_start, mapping_start, mapping_end, destination_start)

                else:
                    continue


        elif not line.strip():
            seeds = seeds | add_set
            seeds = seeds - remove_set - has_mapping
            remove_set.clear()
            add_set.clear()
            has_mapping.clear()

            print(cur_map, seeds)
            assert sum([seed[1] for seed in seeds]) == total_seeds
        else:
            continue

    return min([seed[0] for seed in seeds])

with open('inputs/d5_example') as file:
    # print(p1(file))
    print(p2(file))
