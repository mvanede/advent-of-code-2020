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
        print(f"{idx} - {numbers[idx]} -")
        continue

    v= is_valid(idx, preamble_sz, numbers)
    if  len(v)==0:
        print(f"{idx} -{numbers[idx]} - {len(v)>0}")
        break

n = numbers[:idx]
invalid_number = numbers[idx]


for i in range(len(n)-1):
    for j in range (i+1, len(n)-1):
        contiguous_set = n[i:j]
        s = sum(n[i:j])

        if s == invalid_number:
            print("---------------------------")
            print ("FOUND")
            print(contiguous_set)
            print(max(contiguous_set) + min(contiguous_set))
            print("---------------------------")
        elif s > invalid_number:
            break