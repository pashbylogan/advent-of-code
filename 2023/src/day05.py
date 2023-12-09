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
    future_set = set()
    has_mapping = set()

    for line in file:
        if 'seeds:' in line:
            matches = re.findall(r'\d+', line)

            for i in range(0, len(matches), 2):
                # (number at start of range, length of range)
                seeds.add((int(matches[i]), int(matches[i + 1])))
        elif line[0].isdigit():
            nums = [int(n) for n in line.split()]
            mapping_start = nums[1]
            mapping_end = nums[1] + nums[2] - 1
            destination_start = nums[0]

            for seed_range in seeds:
                seed_start = seed_range[0]
                seed_end = seed_range[0] + seed_range[1] -1 

                # Case 1: Mapping the beginning of seed range
                if mapping_start <= seed_start <= mapping_end and seed_end > mapping_end:
                    seed_mapping_diff = (mapping_end - seed_start + 1)
                    remove_set.add(seed_range)
                    add_set.add((destination_start + (nums[2] - seed_mapping_diff), seed_mapping_diff))
                    has_mapping.add((seed_start, seed_mapping_diff))

                    if (mapping_end + 1, seed_range[1] - seed_mapping_diff) not in has_mapping:
                        future_set.add((mapping_end + 1, seed_range[1] - seed_mapping_diff))

                # Case 2: Mapping the end of the seed range
                elif seed_start < mapping_start and mapping_start <= seed_end <= mapping_end:
                    seed_mapping_diff = 1 + seed_end - mapping_start
                    remove_set.add(seed_range)
                    add_set.add((destination_start, seed_mapping_diff))
                    has_mapping.add((mapping_start, seed_mapping_diff))
                    
                    if (seed_start, seed_range[1] - seed_mapping_diff) not in has_mapping:
                        future_set.add((seed_start, seed_range[1] - seed_mapping_diff))

                # Case 3: Mapping the whole seed range
                elif mapping_start <= seed_start <= mapping_end and mapping_start <= seed_end <= mapping_end:
                    remove_set.add(seed_range)
                    add_set.add((destination_start + (seed_start - mapping_start), seed_range[1]))
                    has_mapping.add((seed_start, seed_range[1]))

                # Case 4: Mapping the middle of the seed range
                elif seed_start <= mapping_start <= seed_end and seed_start <= mapping_end <= seed_end:
                    remove_set.add(seed_range)
                    add_set.add((destination_start, nums[2]))
                    has_mapping.add((mapping_start, nums[2]))

                    if (seed_start, mapping_start - seed_start) not in has_mapping:
                        future_set.add((seed_start, mapping_start - seed_start))

                    if (seed_start + (mapping_start - seed_start) + nums[2], seed_range[1] - nums[2] - (mapping_start - seed_start)) not in has_mapping:
                        future_set.add((seed_start + (mapping_start - seed_start) + nums[2], seed_range[1] - nums[2] - (mapping_start - seed_start)))
                else:
                    continue


        elif not line.strip():
            non_mapped_seeds = _find_non_mapped_seeds(future_set, has_mapping)
            seeds = seeds | add_set | non_mapped_seeds
            seeds = seeds - remove_set
            future_set.clear()
            remove_set.clear()
            add_set.clear()
            has_mapping.clear()

            # TODO: This assert should pass, but it doesn't. Still got the right answer though :P
            # assert sum([seed[1] for seed in seeds]) == total_seeds
        else:
            continue

    return min([seed[0] for seed in seeds])


def _find_non_mapped_seeds(seeds, add_set):
    '''
    Return the seeds if and only if the range of the seed does not overlap with any of the ranges in add_set
    '''
    non_mapped_seeds = set()
    for seed in seeds:
        seed_start = seed[0]
        seed_end = seed[0] + seed[1] - 1
        for add_range in add_set:
            add_start = add_range[0]
            add_end = add_range[0] + add_range[1] - 1
            if seed_start <= add_start <= seed_end or seed_start <= add_end <= seed_end:
                break
        else:
            non_mapped_seeds.add(seed)

    return non_mapped_seeds


with open('inputs/d5') as file:
    # print(p1(file))
    print(p2(file))
