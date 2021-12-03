def str_to_dir(s, x, y):
    if s[0:2] == 'nw':
        x, y = x-1, y+1
        s = s[2:]
    elif s[0:2] == 'sw':
        x, y = x, y-1
        s = s[2:]
    elif s[0:2] == 'ne':
        x, y = x, y+1
        s = s[2:]
    elif s[0:2] == 'se':
        x, y = x+1, y-1
        s = s[2:]
    elif s[0:1] == 'e':
        x, y = x+1, y
        s = s[1:]
    elif s[0:1] == 'w':
        x, y = x-1, y
        s = s[1:]
    else:
        print("UNKNOWN INPUT")
        return

    return str_to_dir(s, x, y) if len(s) else (x, y)


def check_tile(floor_, x, y):
    black_neighbour_cnt = 0
    extended_tiles_to_check=[]
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Only adjacent tiles and not itself
            if i+j in (-2,2) or (i == j == 0):
                continue

            n = (x + i, y + j)
            if n in floor_ and floor_[n] % 2 == 1:
                black_neighbour_cnt += 1
            elif n not in floor_:
                extended_tiles_to_check.append(n)
    return black_neighbour_cnt, extended_tiles_to_check


def should_be_flipped(flipcnt, black_neighbour_cnt):
    return (flipcnt % 2 == 1 and (black_neighbour_cnt == 0 or black_neighbour_cnt > 2)) or (flipcnt % 2 == 0 and black_neighbour_cnt == 2)


def which_should_be_flipped(floor):
    flip_em = []
    edge_tiles = []

    for c, flipcnt in floor.items():
        x, y = c
        black_neighbour_cnt, edge_tiles_of = check_tile(floor, x, y)
        edge_tiles = edge_tiles + edge_tiles_of

        if should_be_flipped(flipcnt, black_neighbour_cnt):
            flip_em.append(c)

    # Process edge tiles
    for c in list(set(edge_tiles)):
        x, y = c
        floor[c] = 0
        black_neighbour_cnt, _ = check_tile(floor, x, y)
        if should_be_flipped(0, black_neighbour_cnt):
            flip_em.append(c)

    return flip_em

def print_floor(floor_, title):
    nr_black = sum(1 for cnt in floor_.values() if cnt % 2 == 1)
    nr_white = sum(1 for cnt in floor_.values() if cnt % 2 == 0)
    print(f"\n -- {title} --")
    print(f"Flipped {nr_black + nr_white} tiles, {nr_black} ended up black, {nr_white} ended up white")


# Read input
f = open("ass-day-24-input.txt", "r")

floor = {}
for line in f.read().split("\n"):
    c = str_to_dir(line, 0, 0)
    floor[c] = floor[c] + 1 if c in floor else 1
print_floor(floor, 'starting sequence')

for day in range(1, 101):
    for t in which_should_be_flipped(floor):
        floor[t] += 1
    print_floor(floor, f'Day {day}')

# Flipped 38647 tiles, 3537 ended up black, 35110 ended up white
