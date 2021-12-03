import copy


class Stack:
    def __init__(self, name):
        self.items = []
        self.name = name

    def repr(self):
        return ','.join([str(i) for i in self.items[::-1]])

    def __str__(self):
        return self.repr()

    def is_empty(self):
        return self.items == []

    def add_to_bottom(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def shorten(self, size):
        self.items = self.items[(self.size() - size):]

    def get_score(self):
        score = 0
        while not self.is_empty():
            score += self.size() * self.pop()

        return score

VERBOSE = False
vprint = print if VERBOSE else lambda *a, **k: None

GAME_COUNT = 1
def play_game(decks_, game=1):
    vprint(f"\n=== Game {game} ===")
    global GAME_COUNT
    previous_rounds = []

    r = 0
    players_in_game = True
    while players_in_game:
        r += 1
        vprint(f"\n-- Round {r} (Game {game}) --")

        recursion_checksum = decks_[0].repr() + decks_[1].repr()
        if recursion_checksum in previous_rounds:
            return 0
        previous_rounds.append(recursion_checksum)

        cards_on_table = []
        nr_cards_greater_equal = True

        for d in decks_:
            vprint(f"{d.name}'s deck: {d}")
            card = d.pop()
            vprint(f"{d.name} plays: {card}")
            cards_on_table.append(card)
            nr_cards_greater_equal = nr_cards_greater_equal and d.size() >= card

        if nr_cards_greater_equal:
            vprint(f"Playing a sub-game to determine the winner...")
            GAME_COUNT += 1
            deck_copy = copy.deepcopy(decks_)
            deck_copy[0].shorten(cards_on_table[0])
            deck_copy[1].shorten(cards_on_table[1])
            winner = play_game(deck_copy, GAME_COUNT)
            vprint(f"\n...anyway, back to game {game}.")
        else:
            winner = cards_on_table.index(max(cards_on_table))

        # Winners card first
        decks_[winner].add_to_bottom(cards_on_table[winner])
        decks_[winner].add_to_bottom(cards_on_table[(winner+1)%2])
        vprint(f"{decks_[winner].name} wins round {r} of game  {game}")
        players_in_game = not (decks_[0].is_empty() or decks_[1].is_empty())

    for idx, d in enumerate(decks_):
        if not d.is_empty():
            vprint(f'{d.name} is the winner of game {game}!')
            return idx


# Read input
f = open("ass-day-22-input.txt", "r")

decks = []
for p in f.read().split("\n\n"):
    lines = p.split('\n')
    s = Stack(lines[0][:-1])
    for card in lines[1:]:
        s.add_to_bottom(int(card))
    decks.append(s)

winner = play_game(decks, 1)
print("\n\n== Post-game results ==")
print(f"Winner is {decks[winner].name}!")
print(f"{decks[0].name} score: {decks[0].get_score()}")
print(f"{decks[1].name} score: {decks[1].get_score()}")
# 32317