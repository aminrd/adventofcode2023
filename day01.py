from tqdm import tqdm

DEBUG = False
PART_NUMBER = 2
input_file = "inputs/test.txt" if DEBUG else "inputs/day1.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

mapper = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0"
}


def map_values(line):
    digit_indices = []
    for i, c in enumerate(line):
        if c.isdigit():
            digit_indices.append(i)

    if len(digit_indices) > 1:
        line = line[:digit_indices[0] + 1] + line[digit_indices[-1]:]

    while True:
        candidates = []
        for k, v in mapper.items():
            ind = line.find(k)
            if ind < 0: continue
            candidates.append((ind, k, v))
        if len(candidates) < 1:
            return line

        _, k, v = sorted(candidates)[0]
        line = line.replace(k, v, 1)


def get_digits(line):
    if PART_NUMBER == 2:
        line = map_values(line)
    return [int(c) for c in line if c.isdigit()]


def combine_first_and_last(digits):
    if len(digits) < 1:
        return 0
    return digits[0] * 10 + digits[-1]


total = 0
for line in lines:
    digits = get_digits(line)
    total += combine_first_and_last(digits)

print(f"Answer = {total}")
