hand_strength_map = {
    'five': 7,
    'four': 6,
    'full': 5,
    'three': 4,
    'two': 3,
    'one': 2,
    'high': 1,
}

card_strength_map = {
    'J': 1, # 11 in p1
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def _get_hand_strength_p2(hand):
    char_map = {}

    for c in hand:
        char_map[c] = char_map.get(c, 0) + 1

    filtered_map = {k: v for k, v in char_map.items() if k != 'J'}.values()

    # Five of a kind
    if 5 in char_map.values() or (5 - char_map.get('J', 0)) in filtered_map:
        strength = 7
    # Four of a kind
    elif 4 in char_map.values() or (4 - char_map.get('J', 0)) in filtered_map:
        strength = 6
    # Full house
    elif (3 in char_map.values() and 2 in char_map.values()) or \
            (list(char_map.values()).count(2) == 2 and \
            char_map.get('J', 0) == 1):
        strength = 5
    # Three of a kind
    elif 3 in char_map.values() or (3 - char_map.get('J', 0)) in filtered_map:
        strength = 4
    # Two pair
    elif list(char_map.values()).count(2) == 2 or \
            (2 in filtered_map and \
            (2 - char_map.get('J', 0)) in [v for v in filtered_map if v != 2]):
        strength = 3
    # One pair
    elif 2 in char_map.values() or (2 - char_map.get('J', 0)) in filtered_map:
        strength = 2
    # High card
    else:
        strength = 1

    return strength


def _get_hand_strength_p1(hand):
    char_map = {}

    for c in hand:
        char_map[c] = char_map.get(c, 0) + 1

    # Five of a kind
    if 5 in char_map.values():
        strength = 7
    # Four of a kind
    elif 4 in char_map.values():
        strength = 6
    # Full house
    elif (3 in char_map.values() and 2 in char_map.values()):
        strength = 5
    # Three of a kind
    elif 3 in char_map.values():
        strength = 4
    # Two pair
    elif list(char_map.values()).count(2) == 2:
        strength = 3
    # One pair
    elif 2 in char_map.values():
        strength = 2
    # High card
    else:
        strength = 1

    return strength


def _compare_hands(hand1, hand2):
    for i in range(len(hand1)):
        if card_strength_map[hand1[i]] > card_strength_map[hand2[i]]:
            return True
        elif card_strength_map[hand1[i]] < card_strength_map[hand2[i]]:
            return False


def p1(file):
    answer = []
    hand_to_bid = {}

    for line in file:
        hand, bid = line.split()
        answer.append((hand, _get_hand_strength_p1(hand)))
        hand_to_bid[hand] = int(bid)

    # Custom selection sort
    for i in range(len(answer)):
        min_idx = i
        for j in range(i+1, len(answer)):
            if answer[min_idx][1] > answer[j][1]:
                min_idx = j
            elif answer[min_idx][1] == answer[j][1]:
                if _compare_hands(answer[min_idx][0], answer[j][0]):
                    min_idx = j

        answer[i], answer[min_idx] = answer[min_idx], answer[i]

    return sum([hand_to_bid[x[0]] * (i+1) for i, x in enumerate(answer)])


def p2(file):
    answer = []
    hand_to_bid = {}

    for i, line in enumerate(file):
        hand, bid = line.split()
        answer.append((hand, _get_hand_strength_p2(hand)))
        hand_to_bid[hand] = int(bid)

    # Custom selection sort
    for i in range(len(answer)):
        min_idx = i
        for j in range(i+1, len(answer)):
            if answer[min_idx][1] > answer[j][1]:
                min_idx = j
            elif answer[min_idx][1] == answer[j][1]:
                if _compare_hands(answer[min_idx][0], answer[j][0]):
                    min_idx = j

        answer[i], answer[min_idx] = answer[min_idx], answer[i]

    return sum([hand_to_bid[x[0]] * (i+1) for i, x in enumerate(answer)])


with open('inputs/d7') as file:
    # print(p1(file))
    print(p2(file))
