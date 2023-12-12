import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day11.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

part_one = None
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")

