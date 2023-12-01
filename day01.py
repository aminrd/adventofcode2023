from tqdm import tqdm

DEBUG = 1
PART_NUMBER = 1
input_file = "inputs/test.txt" if DEBUG else "inputs/day1.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

