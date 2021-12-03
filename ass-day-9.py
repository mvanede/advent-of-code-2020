from itertools import combinations




def is_valid(idx, preamble_size, sequence):
    if idx<preamble_size:
        return None

    preamble = sequence[idx-preamble_size:idx]
    cmbnts = [pair for pair in combinations(preamble, 2) if sum(pair) == sequence[idx]]
    return cmbnts


# Read input
f = open("ass-day-9-input.txt", "r")
lines = f.read().split("\n")
numbers = [int(line) for line in lines]

preamble_sz = 25
for idx, n in enumerate(numbers):
    if idx<preamble_sz:
        print(f"{numbers[idx]} -")
        continue

    print(f"{numbers[idx]} - {len(is_valid(idx, preamble_sz, numbers))>0}")
