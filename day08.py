import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day08.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# line : AAA = (BBB, CCC)
# Left = 0, Right = 1
class Node:
    def __init__(self, line: str):
        node_id, adjs = line.split("=")
        self.id = node_id.strip()
        left, right = adjs.replace("(", "").replace(")", "").split(",")
        self.adj = [left.strip(), right.strip()]

nodes = dict()
path = [0 if c == "L" else 1 for c in lines[0]]

for line in lines[1:]:
    if len(line) < 1:
        continue
    node = Node(line)
    nodes[node.id] = node

target = "ZZZ"
state = "AAA"
t = 0

while state != target:
    p = path[t % len(path)]
    t += 1
    state = nodes[state].adj[p]

part_one = t
print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")
