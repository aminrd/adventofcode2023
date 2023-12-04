DEBUG = False
PART_NUMBER = 1
input_file = "inputs/test.txt" if DEBUG else "inputs/day4.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


class Card:
    def __init__(self, line):
        card_part, rest = line.split(':')
        self.index = int(card_part.strip()[5:])
        winning, guess = rest.split('|')
        self.winning = set(map(int, winning.strip().split()))
        self.guess = set(map(int, guess.strip().split()))

    def get_match_cnt(self):
        return sum(guess in self.winning for guess in self.guess)

    def get_points(self):
        cnt = self.get_match_cnt()
        return 0 if cnt == 0 else 2 ** (cnt - 1)


cards = [Card(line) for line in lines]

part_one = sum(card.get_points() for card in cards)
print(f"Part one = {part_one}")

part_two = 0
weights = [1] * len(cards)
for i, card in enumerate(cards):
    for j in range(card.get_match_cnt()):
        if (i+j+1) < len(cards):
            weights[i+j+1] += weights[i]

print(f"Part two = {sum(weights)}")