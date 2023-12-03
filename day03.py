from collections import defaultdict

DEBUG = False
PART_NUMBER = 1
input_file = "inputs/test.txt" if DEBUG else "inputs/day3.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

Directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))

class Symbol:
    def __init__(self, symbol, i, j):
        self.s = symbol
        self.index = (i, j)
        self.shadow = set((i+di, j+dj) for di, dj in Directions)

    def get_line(self):
        return self.index[0]

    def get_shadows(self):
        return self.shadow

    def is_gear(self):
        return self.s == "*"

class Number:
    def __init__(self, s_value, i, j):
        self.start_index = (i, j)
        self.length = len(s_value)
        self.value = int(s_value)

    def get_line(self):
        return self.start_index[0]

    def next_to_any_symbol(self, shaodws):
        i, j = self.start_index
        return any((i, j+dj) in shaodws for dj in range(self.length))

    def next_to_symbol(self, symbol: Symbol):
        i, j = self.start_index
        return any((i, j+dj) in symbol.get_shadows() for dj in range(self.length))

symbols = []
numbers = []

for i, line in enumerate(lines):
    num = ""
    for j, c in enumerate(line):
        if c == '.':
            continue
        elif not c.isdigit():
            symbols.append(Symbol(c, i, j))
        else:
            num += c
            if j == len(line) - 1 or not line[j+1].isdigit():
                numbers.append(Number(num, i, j - len(num) + 1))
                num = ""

symbol_shadow = defaultdict(bool)
for symbol in symbols:
    for shadow in symbol.get_shadows():
        symbol_shadow[shadow] = True

part_one = sum(number.value for number in numbers if number.next_to_any_symbol(symbol_shadow))
print(f"Part one = {part_one}")

numbers_per_line = defaultdict(list)
for number in numbers:
    numbers_per_line[number.get_line()].append(number)

part_two = 0
for symbol in symbols:
    if not symbol.is_gear():
        continue

    adj_nums = []
    s_line = symbol.get_line()
    for lnumber in range(s_line-1, s_line+2):
        for number in numbers_per_line[lnumber]:
            if number.next_to_symbol(symbol):
                adj_nums.append(number)

    if len(adj_nums) == 2:
        part_two += adj_nums[0].value * adj_nums[1].value

print(f"Part two = {part_two}")
