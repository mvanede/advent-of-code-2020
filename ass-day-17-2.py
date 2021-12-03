import numpy as np
import copy

def get_neighbours(x, y, z, w, space_, radius=1):
    neighbours = []
    for idx in range(-1, 2):
        for idy in range(-1, 2):
            for idz in range(-1, 2):
                for idw in range(-1, 2):
                    if not (idx==0 and idy==0 and idz==0 and idw==0):
                        try:
                            neighbours.append(space_[x+idx, y+idy, z+idz, w+idw])
                        except IndexError as e:
                            continue
    return neighbours


# First loop
def run_cycle(space):
    old_space = copy.deepcopy(space)
    active_cell_count = 0

    for x in range(old_space.shape[0]):
        for y in range(old_space.shape[1]):
            for z in range(old_space.shape[2]):
                for w in range(old_space.shape[3]):
                    neighbours = get_neighbours(x, y, z, w, old_space)
                    if old_space[x, y, z, w] == '#' and not (2<=neighbours.count('#')<=3):
                        space[x, y, z, w] = '.'
                    elif neighbours.count('#') == 3:
                        space[x, y, z, w] = '#'

                    active_cell_count += 1 if space[x, y, z, w] == '#' else 0
    return active_cell_count


# Read input
f = open("ass-day-17-input.txt", "r")
lines = f.read().split("\n")
input = [list(line) for line in lines]

nr_cycles = 6
init_size = len(input[0])
cube_size= (nr_cycles*2)+init_size
zero_offset = nr_cycles


# Create space, empty all cells
space = np.zeros((cube_size,cube_size,cube_size, cube_size), dtype='U1') # Make a 10 by 20 by 30 array

# Init space with input
for idx, x in enumerate(input):
    for idy, y in enumerate(x):
        for idz, z in enumerate(y):
            space[idx+zero_offset, idy+zero_offset, idz+zero_offset, zero_offset] = z


# Run cycles
for r in range(0, nr_cycles):
    active_cell_count = run_cycle(space)


print(f"Done. Active cells: {active_cell_count}")