from tqdm import tqdm

DEBUG = True
PART_NUMBER = 1
input_file = "inputs/test.txt" if DEBUG else "inputs/day1.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def get_digits(line):
    if PART_NUMBER == 1:
        return [int(c) for c in line if c.isdigit()]
    else:
        

def combine_first_and_last(digits):
    return digits[0] * 10 + digits[-1]

part_one_sum = 0
for line in lines:
    digits = get_digits(line)
    part_one_sum += combine_first_and_last(digits)

print(f"Part one = {part_one_sum}")


mapper = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

