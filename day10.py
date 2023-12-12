import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day10.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

M, N = len(lines), len(lines[0])


def valid_index(x, y):
    return 0 <= x < M and 0 <= y < N


class Node:
    def __init__(self, i, j):
        self.index = (i, j)
        self.adjs = []
        self.dist = None

    def add_adj(self, i, j):
        if (i, j) not in self.adjs:
            self.adjs.append((i, j))

    def validate(self):
        if self.index is None:
            raise Exception("Index is None")

        return valid_index(self.index[0], self.index[1]) and self.adjs is not None and len(self.adjs) <= 2

    def __repr__(self):
        return f"Node at {self.index}, adj = {self.adjs}"

    def __str__(self):
        return self.__repr__()


class Graph:
    def __init__(self, lines):
        self.start = None

        self.graph = []
        for i in range(M):
            self.graph.append([Node(i, j) for j in range(N)])

        def connect(n1, n2):
            i1, j1 = n1
            i2, j2 = n2

            if valid_index(i1, j1) and valid_index(i2, j2):
                self.graph[i1][j1].add_adj(i2, j2)

                if (i2, j2) == self.start:
                    self.graph[i2][j2].add_adj(i1, j1)

        for i, line in enumerate(lines):
            if (j := line.find("S")) >= 0:
                self.start = (i, j)
                self.graph[i][j].dist = 0
                break

        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == '.':
                    continue
                elif c == "S":
                    continue
                elif c == "-":
                    connect((i, j), (i, j + 1))
                    connect((i, j), (i, j - 1))
                elif c == "|":
                    connect((i, j), (i + 1, j))
                    connect((i, j), (i - 1, j))
                elif c == "L":
                    connect((i, j), (i - 1, j))
                    connect((i, j), (i, j + 1))
                elif c == "7":
                    connect((i, j), (i + 1, j))
                    connect((i, j), (i, j - 1))
                elif c == "F":
                    connect((i, j), (i + 1, j))
                    connect((i, j), (i, j + 1))
                elif c == "J":
                    connect((i, j), (i - 1, j))
                    connect((i, j), (i, j - 1))

        self.validate()

    def validate(self):
        for row in self.graph:
            for node in row:
                if not node.validate():
                    raise Exception(f"Not valid! {node}")

    def traverse(self):
        node = self.graph[self.start[0]][self.start[1]]
        node.dist = 0
        bfs = [node]

        max_d = 0
        farthest_node = node

        while len(bfs) > 0:
            node = bfs.pop(0)

            if node.dist is not None and node.dist > max_d:
                max_d = node.dist
                farthest_node = node

            for ai, aj in node.adjs:
                node_adj = self.graph[ai][aj]
                if node_adj.dist is None:
                    node_adj.dist = node.dist + 1
                    bfs.append(node_adj)

        return farthest_node

    def print_distances(self):
        for row in self.graph:
            distances = ["{:3d}".format(node.dist) if node.dist is not None else " * " for node in row]
            print(" ".join(distances))


G = Graph(lines)
far_node = G.traverse()

if DEBUG:
    G.print_distances()

part_one = far_node.dist
print(f"Part one = {part_one}")


directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
outsides = set()
for i in range(-1, M+1):
    outsides.add((i, 0))
    outsides.add((i, N))

for j in range(-1, N+1):
    outsides.add((0, j))
    outsides.add((M, j))

queue = list(outsides)
while len(queue) > 0:
    i, j = queue.pop(0)
    for di, dj in directions:
        ai, aj = i+di, j+dj
        if valid_index(ai, aj) and (ai, aj) not in outsides and G.graph[ai][aj].dist is None:
            outsides.add((ai, aj))
            queue.append((ai, aj))

part_two = 0
for i in range(M):
    for j in range(N):
        if (i, j) not in outsides and G.graph[i][j].dist is None:
            part_two += 1

print(f"Part two = {part_two}")
