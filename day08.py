import math
import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day08.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# line : AAA = (BBB, CCC)
# Left = 0, Right = 1
nodes = dict()
class Node:
    def __init__(self, line: str):
        node_id, adjs = line.split("=")
        self.id = node_id.strip()
        left, right = adjs.replace("(", "").replace(")", "").split(",")
        self.adj = [left.strip(), right.strip()]

    def next(self, p):
        return nodes[self.adj[p]]

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
    if state not in nodes:
        break
    p = path[t % len(path)]
    state = nodes[state].adj[p]
    t += 1

part_one = t
print(f"Part one = {part_one}")

t = 0
t_max = 10 ** 30
states = [node for node in nodes.values() if node.id.endswith("A")]

def get_count_for_state(node: Node):
    t = 0
    while not node.id.endswith("Z"):
        p = path[t % len(path)]
        node = node.next(p)
        t += 1
    return t

counts = [get_count_for_state(state) for state in states]
lcm = counts[0]
for count in counts[1:]:
    lcm = (lcm * count) // math.gcd(lcm, count)

part_two = lcm
print(f"Part two = {part_two}")
