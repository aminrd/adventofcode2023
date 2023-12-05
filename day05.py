import bisect
import math
from tqdm import tqdm

DEBUG = False
input_file = "inputs/test.txt" if DEBUG else "./inputs/day05.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


class Table:
    def __init__(self, maps: list[str], table_name: str):
        self.table_name = table_name
        self.hash_table = dict()

        maps_integers = [tuple(map(int, line.split())) for line in maps]
        map_list = [(src, src + rng - 1, dst) for dst, src, rng in maps_integers]
        self.maps = list(sorted(map_list))
        self.min_possible = min(s for s, _, _ in self.maps)
        self.max_possible = max(e for _, e, _ in self.maps)

    def get_value_not_optimized(self, query):
        for start, end, dst in self.maps:
            if start <= query <= end:
                return (query - start) + dst
        return query

    def get_value(self, src):

        if src in self.hash_table:
            return self.hash_table[src]

        query = (src, math.inf, math.inf)
        index = bisect.bisect_left(self.maps, query)

        if index == 0:
            self.hash_table[src] = src
            return src
        if index == len(self.maps):
            index -= 1

        while index >= 0:
            start, end, dst = self.maps[index]
            if start <= src <= end:
                self.hash_table[src] = (src - start) + dst
                return self.hash_table[src]
            index -= 1

        self.hash_table[src] = src
        return src

    def get_range_values(self, q_start, q_end, results=None):
        if results is None:
            results = []

        if q_start == q_end:
            single_query = self.get_value_not_optimized(q_start)
            results.append((single_query, single_query))
            return results

        ind = 0
        covered_query = q_start
        while covered_query < q_end:
            if ind >= len(self.maps):
                results.append((covered_query, q_end))
                covered_query = q_end
                continue

            start, end, dst = self.maps[ind]
            if end < covered_query:
                ind += 1
            elif covered_query < start:
                results.append((covered_query, start - 1))
                covered_query = start
            else:
                e = min(q_end, end)
                results.append((covered_query - start + dst, e - start + dst))
                covered_query = e + 1
                ind += 1

        return results


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

part_two = math.inf
for i in range(len(seeds) // 2):
    queires = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1])]
    for table_name in table_names:
        new_queries = []
        for query_start, query_end in queires:
            tables[table_name].get_range_values(query_start, query_end, new_queries)
        queires = new_queries

    min_loc = min(lstart for lstart, lend in queires)
    part_two = min(part_two, min_loc)

print(f"Part two = {part_two}")
