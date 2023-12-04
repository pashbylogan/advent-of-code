def p1(file):
    answer = 0

    for line in file:
        both_cards = line.split(': ')[1]
        winning_nums = set(both_cards.split(' | ')[0].split())
        player_nums = set(both_cards.split(' | ')[1].split())

        answer += 2**(len(winning_nums & player_nums)-1) if len(winning_nums & player_nums) > 0 else 0

    return answer


def p2(file):
    answer = 0
    num_dups = {}

    for i, line in enumerate(file):
        answer += num_dups.get(i+1, 1)

        both_cards = line.split(': ')[1]
        winning_nums = set(both_cards.split(' | ')[0].split())
        player_nums = set(both_cards.split(' | ')[1].split())

        win_count = len(winning_nums & player_nums)

        for j in range(win_count):
            cur_count = num_dups.get(i+j+2, 1)
            num_dups[i+j+2] = cur_count + num_dups.get(i+1, 1)

    return answer

with open('inputs/d4') as file:
    # print(p1(file))
    print(p2(file))
