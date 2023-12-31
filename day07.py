import sys

DEBUG = sys.gettrace() is not None
input_file = "inputs/test.txt" if DEBUG else "./inputs/day07.txt"
with open(input_file) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

mapper = {
    "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

mapper2 = {
    "A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

# Types:
# 1 : all of a kind
# 2 : four of a kind
# 3 : full house
# 4 : three of a kind
# 5 : two pairs
# 6 : one pair

cnt_to_type = {
    (5,): 1,
    (4, 1): 2,
    (3, 2): 3,
    (3, 1, 1): 4,
    (2, 2, 1): 5,
    (2, 1, 1, 1): 6,
    (1, 1, 1, 1, 1): 7
}


class HandBase:
    def __init__(self, cards: str, bid: str, card_mapper: dict):
        self.cards_main = cards
        self.bid = int(bid.strip())
        self.cards = tuple(card_mapper[c] for c in cards.strip())
        self.type = None

    def get_win(self, rank):
        return self.bid * rank

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.type > other.type: return True
        if self.type < other.type: return False

        for a, b in zip(self.cards, other.cards):
            if a < b:
                return True
            elif a > b:
                return False
        return False


class Hand(HandBase):
    def __init__(self, cards: str, bid: str):
        super().__init__(cards, bid, mapper)

        cnt = [0] * 20
        for c in self.cards:
            cnt[c] += 1
        cnt = tuple(sorted([count for count in cnt if count != 0], reverse=True))
        self.type = cnt_to_type[cnt]


class Hand2(HandBase):
    def __init__(self, cards: str, bid: str):
        super().__init__(cards, bid, mapper2)

        cnt = [0] * 20
        for c in self.cards:
            cnt[c] += 1

        cj = cnt[mapper2["J"]]
        cnt[mapper2["J"]] = 0
        if cj >= 4:
            self.type = 1
            return

        cnt = sorted(cnt, reverse=True)
        if cj > 0:
            cnt[0] += cj
        cnt = tuple([count for count in cnt if count != 0])
        self.type = cnt_to_type[cnt]


hands = []
hands2 = []
for line in lines:
    card_string, bid_string = line.split()
    hands.append(Hand(card_string, bid_string))
    hands2.append(Hand2(card_string, bid_string))

part_one = 0
for rank, hand in enumerate(sorted(hands)):
    part_one += hand.get_win(rank + 1)

print(f"Part one = {part_one}")

part_two = 0
for rank, hand in enumerate(sorted(hands2)):
    part_two += hand.get_win(rank + 1)

print(f"Part two = {part_two}")
