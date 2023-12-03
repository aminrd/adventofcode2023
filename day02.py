DEBUG = False
PART_NUMBER = 1
input_file = "inputs/test.txt" if DEBUG else "inputs/day2.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

color_index = {
    "red": 0,
    "green": 1,
    "blue": 2
}

def vector_lte(V1, V2):
    return all(v1 <= v2 for v1, v2 in zip(V1, V2))

class Game:
    def __init__(self, line):
        gpart, rest = line.split(':')
        self.index = int(gpart[5:])
        self.buckets = []

        buckets_string = rest.strip().split(';')
        for bucket_string in buckets_string:
            colors = [0] * 3
            colors_string = bucket_string.strip().split(',')
            for color_string in colors_string:
                cnt, cname = color_string.strip().split()
                ind = color_index[cname.strip()]
                colors[ind] = int(cnt)

            self.buckets.append((tuple(colors)))

    def all_smaller_than_setup(self, setup=(12, 13, 14)):
        return all(vector_lte(bucket, setup) for bucket in self.buckets)

    def get_max_multiplied(self):
        color_max = [0] * 3
        for bucket in self.buckets:
            color_max = [max(cmax, b) for cmax, b in zip(color_max, bucket)]

        max_mult = 1
        for cmax in color_max:
            if cmax != 0:
                max_mult *= cmax
        return max_mult

games = [Game(line) for line in lines]
part_one = sum(game.index for game in games if game.all_smaller_than_setup())
print(f'Part one = {part_one}')

part_two = sum(game.get_max_multiplied() for game in games)
print(f'Part two = {part_two}')