import re

digit_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
}

with open('inputs/day01.txt') as file:
    sum = 0
    for j, line in enumerate(file):
        num = ''
        num_idx = []

        for i, char in enumerate(line):
            if char.isdigit():
                num_idx.append((i, char))

        for word in digit_words.keys():
            try:
                sub_idx_arr = [m.start() for m in re.finditer(word, line)]
                
                for k in sub_idx_arr:
                    num_idx.append((k, digit_words[word]))
            except:
                continue

        num_idx.sort(key = lambda a: a[0])

        if len(num_idx) > 1:
            num = num_idx[0][1] + num_idx[-1][1]
        elif len(num_idx) == 1:
            num = num_idx[0][1] + num_idx[0][1]

        sum += int(num)
        num = ''

    print(sum)
