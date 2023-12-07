import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day07.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

mapper = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

# Types:
# 1 : all of a kind
# 2 : four of a kind
# 3 : full house
# 4 : three of a kind
# 5 : two pairs
# 6 : one pair

class Hand:
    def __init__(self, cards: str, bid: str):
        self.cards_main = cards
        self.cards = tuple(mapper[c] for c in cards.strip())
        self.type = None
        self.bid = int(bid.strip())

        cnt = [0] * 20
        for c in self.cards:
            cnt[c] += 1
        cnt = tuple(sorted([count for count in cnt if count != 0], reverse=True))

        if cnt == (5,):
            self.type = 1
        elif cnt == (4, 1):
            self.type = 2
        elif cnt == (3,2):
            self.type = 3
        elif cnt == (3, 1, 1):
            self.type = 4
        elif cnt == (2, 2, 1):
            self.type = 5
        elif cnt == (2, 1, 1, 1):
            self.type = 6
        else:
            self.type = 7

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.type > other.type:
            return True
        if self.type < other.type:
            return False

        for a, b in zip(self.cards, other.cards):
            if a < b:
                return True
            elif a > b:
                return False

        return False

hands = []
for line in lines:
    card_string, bid_string = line.split()
    hands.append(Hand(card_string, bid_string))

part_one = 0
for rank, hand in enumerate(sorted(hands)):
    part_one += hand.bid * (rank + 1)

print(f"Part one = {part_one}")

part_two = None
print(f"Part two = {part_two}")

