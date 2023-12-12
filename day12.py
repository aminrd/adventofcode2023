import sys
from collections import defaultdict

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day12.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


class Msg:
    def __init__(self, line):
        self.msg, numbers = line.strip().split()
        self.numbers = list(map(int, numbers.split(',')))


def get_pattern(msg):
    return [len(part) for part in msg.split('.') if len(part) > 0]

def new_msg(msg, i, char):
    return msg[:i] + char + msg[i+1:]

cache = defaultdict(int)

def count_ways(msg: str, nums: list):
    if len(msg) < 0:
        return 0

    if len(nums) < 1:
        return 0 if "#" in msg else 1

    key = (msg, tuple(nums))
    if key in cache:
        return cache[key]

    i_q = msg.find("?")
    if i_q < 0:
        cache[key] = get_pattern(msg) == nums
        return cache[key]
    elif i_q == 0 or msg[i_q-1] == "#":
        cache[key] += count_ways(new_msg(msg, i_q, "#"), nums)
        cache[key] += count_ways(new_msg(msg, i_q, "."), nums)
        return cache[key]

    part_one, rest = msg[:i_q], msg[i_q:]
    p1 = get_pattern(part_one)
    if len(p1) > len(nums) or p1 != nums[:len(p1)]:
        cache[key] = 0
        return cache[key]

    cache[key] = count_ways(rest, nums[len(p1):])
    return cache[key]

messages = [Msg(line) for line in lines]
part_one = sum(count_ways(msg.msg, msg.numbers) for msg in messages)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
