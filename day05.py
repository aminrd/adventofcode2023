import bisect
import math

DEBUG = False
input_file = "inputs/test.txt" if DEBUG else "./inputs/day05.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


class Table:
    def __init__(self, maps: list[str], table_name: str):
        self.table_name = table_name

        maps_integers = [tuple(map(int, line.split())) for line in maps]
        map_list = [(src, src + rng - 1, dst) for dst, src, rng in maps_integers]
        self.maps = list(sorted(map_list))

    def get_value_not_optimized(self, query):
        for start, end, dst in self.maps:
            if start <= query <= end:
                return (query - start) + dst
        return query

    def get_value(self, src):
        query = (src, math.inf, math.inf)
        index = bisect.bisect_left(self.maps, query)

        if index == 0:
            return src
        if index == len(self.maps):
            index -= 1

        while index >= 0:
            start, end, dst = self.maps[index]
            if start <= src <= end:
                return (src - start) + dst
            index -= 1
        return src

seeds = list(map(int, lines[0].replace("seeds: ", "").strip().split()))
table_names = (
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location"
)
tables = dict()

line_index = 1
while line_index < len(lines):
    line = lines[line_index]
    if len(line) < 1:
        line_index += 1
        continue

    if any(table_name in line for table_name in table_names):
        table_name = [table_name for table_name in table_names if table_name in line][0]
        maps = []
        line_index += 1
        while line_index < len(lines) and len(lines[line_index]) > 0 and lines[line_index][0].isdigit():
            maps.append(lines[line_index])
            line_index += 1

        tables[table_name] = Table(maps, table_name)


locations = []
for seed in seeds:
    query = seed
    for table_name in table_names:
        query = tables[table_name].get_value_not_optimized(query)
    locations.append(query)

part_one = min(locations)
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
