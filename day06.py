import sys
import math

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day06.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def get_nums(key: str, line: str):
    num_part = line.replace(key, "").strip()
    return list(map(int, num_part.split()))

def get_dist(t_charge, t_total):
    return (t_total - t_charge) * t_charge

def count_ways(t: int, d: int):
    return sum(get_dist(t_charge, t) > d for t_charge in range(t+1))

# Solving X^2 - TX + D < 0
def count_ways_fast(t: int, d: int):
    x1 = (t - math.sqrt(t ** 2 - 4 * d)) / 2 + 0.001
    x2 = (t + math.sqrt(t ** 2 - 4 * d)) / 2 - 0.001
    return math.ceil(x2) - math.floor(x1) - 1


times = get_nums("Time: ", lines[0])
dist = get_nums("Distance: ", lines[1])

part_one = 1
for t, d in zip(times, dist):
    ways = count_ways(t, d)
    part_one *= ways
print(f"Part one = {part_one}")

T = int("".join(str(t) for t in times))
D = int("".join(str(d) for d in dist))
part_two = count_ways_fast(T, D)
print(f"Part two = {part_two}")
