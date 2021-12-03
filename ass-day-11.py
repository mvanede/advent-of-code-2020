import copy

# Generate current state for each seat

def pretty_print(matrix):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
    print("\n------------------------------------------\n")

def get_hash(seat_plan):
    hash = ''
    for row in seat_plan:
        hash += ''.join(row)
    return hash


def get_surroundings(idxr, idxs, current_state):
    surrounding_seats = []

    for y in range(max(0, idxr - 1), min(idxr + 2, len(current_state))):
        for x in range(max(0, idxs-1), min(idxs+2, len(current_state[y]))):
            #Don't add yourself
            if not (y == idxr and x == idxs):
                surrounding_seats.append(current_state[y][x])

    return surrounding_seats


def get_new_seat_occupation(idxr, idxs, current_state):
    surrounding_seats = get_surroundings(idxr, idxs, current_state)
    state = current_state[idxr][idxs]
    # print(f"get_new_seat_occupation({idxr},{idxs}), current_state={state}, surrounding_seats={surrounding_seats}")

    if state == 'L' and not '#' in surrounding_seats:
        return '#'
    elif state == '#':
        if sum(1 for x in surrounding_seats if x == '#') >=4:
            return 'L'

    return state


def get_next_state(current_state):
    next_state = copy.deepcopy(current_state)

    for idxr, row in enumerate(current_state):
        for idxs, seat in enumerate(row):
            next_state[idxr][idxs] = get_new_seat_occupation(idxr, idxs, current_state)

    return next_state

# Read input
f = open("ass-day-11-input.txt", "r")
lines = f.read().split("\n")
seat_plan = [list(line) for line in lines]


# Repeat
current_state = seat_plan
new_state = get_next_state(seat_plan)

iteration =0
while get_hash(current_state) != get_hash(new_state):
    # print(f"Iteration: {iteration}")
    current_state = new_state
    new_state = get_next_state(current_state)
    iteration +=1


print(f"Done.Iterated {iteration} times. Occupied seats {sum(1 for x in get_hash(new_state) if x == '#')}")
pretty_print(new_state)
