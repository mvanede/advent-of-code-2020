from pprint import pprint
import itertools

class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def __str__(self):
        return ','.join([str(i) for i in self.items[::-1]])

    def is_empty(self):
        return self.items == []

    def add_to_bottom(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_score(self):
        score = 0
        while not self.is_empty():
            score += self.size() * self.pop()
        return score

# Read input
f = open("ass-day-22-input.txt", "r")

decks = []
for p in f.read().split("\n\n"):
    lines = p.split('\n')
    s = Stack(lines[0][:-1])
    for card in lines[1:]:
        s.add_to_bottom(int(card))
    decks.append(s)


def play_round(decks_):
    cards_on_table = []
    for d in decks_:
        print(f"{d.name}'s deck: {d}")
        card = d.pop()
        print(f"{d.name} plays: {card}")
        cards_on_table.append(card)

    winner = cards_on_table.index(max(cards_on_table))
    print(f"{decks_[winner].name} wins the round!\n")

    cards_on_table.sort(reverse=True)
    for c in cards_on_table:
        decks_[winner].add_to_bottom(c)


players_in_game = len(decks)
r = 1

while players_in_game > 1:
    print(f"-- Round {r} --")
    play_round(decks)
    players_in_game = sum(1 for d in decks if not d.is_empty())
    r += 1

print(f"== Post-game results ==")
for idx, d in enumerate(decks):
    print(f"{d.name}'s deck: {d}")
    if not d.is_empty():
        print(f'{d.name} is the final winner. Score: {d.get_score()}')

# 35202