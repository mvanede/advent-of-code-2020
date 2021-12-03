import math
import copy


def create_tile_lib(tiles_txt):
    tile_edges_lib = {}
    tile_full_lib = {}
    for tile in tiles_txt:
        t = tile.split("\n")
        tid = t[0][5:-1]
        tile_full_lib[tid] = [list(r) for r in t[1:]]
        tile_edges_lib[tid] = [t[1:][0], ''.join([x[-1:] for x in t[1:]]), t[1:][-1:][0], ''.join([x[:1] for x in t[1:]])]
    return tile_edges_lib, tile_full_lib


def rotate_tile_r(tile_):
    top_, right_, bottom_, left_ = tile_
    return [left_[::-1], top_, right_[::-1], bottom_]


def flip_tile(tile_, flip_):
    top_, right_, bottom_, left_ = tile_
    if flip_ == 'H': return [top_[::-1], left_, bottom_[::-1], right_]
    if flip_ == 'V': return [bottom_, right_[::-1], top_, right_[::-1]]
    return tile_


def rotate_tile(tile_, orientation_):
    rotate_, flip_ = orientation_
    while rotate_:
        tile_ = rotate_tile_r(tile_)
        rotate_ -= 1
    return flip_tile(tile_, flip_)


def rotate_full_tile_r(tile_):
    rotated_tile = copy.deepcopy(tile_)
    size_ = len(tile_)

    for i in range (0, size_):
        for j in range (0, size_):
            rotated_tile[i][j] = tile_[-(j + 1)][i][:]
    return rotated_tile


def flip_full_tile_h(tile_):
    flipped_tile = copy.deepcopy(tile_)
    size_ = len(tile_)

    for i in range (0, size_):
        for j in range (0, size_):
            flipped_tile[i][size_-(j+1)] = tile_[i][j]
    return flipped_tile


def flip_full_tile_v(tile_):
    flipped_tile = copy.deepcopy(tile_)
    size_ = len(tile_)

    for i in range (0, size_):
        flipped_tile[size_-(i+1)] = tile_[i]
    return flipped_tile


def flip_full_tile(fulltile_, flip_):
    if flip_ == 'H': return flip_full_tile_h(fulltile_)
    if flip_ == 'V': return flip_full_tile_v(fulltile_)
    return fulltile_


def rotate_full_tile(fulltile_, orientation_):
    rotate_, flip_ = orientation_
    while rotate_:
        fulltile_ = rotate_full_tile_r(fulltile_)
        rotate_ -= 1

    return flip_full_tile(fulltile_, flip_)

def preprocess_tile(tile_):
    r = {}
    for _ in range(0, 4):
        for f in ['.', 'H', 'V']:
            t = rotate_tile(tile_, (_, f))
            r[''.join((str(_), f))] = t
    return r


def create_edge_lookup(tile_lib):
    edge_lookup_ = dict(zip(range(0, 4), [{}, {}, {}, {}]))

    for tid_ in tile_lib:
        tile_ = tile_lib[tid_]
        pt_ = preprocess_tile(tile_)

        for orientation_ in pt_:
            edges_ = pt_[orientation_]
            for idx_, edge_ in enumerate(edges_):
                if not edge_ in edge_lookup_[idx_]:
                    edge_lookup_[idx_][edge_] = []
                edge_lookup_[idx_][edge_].append(tid_+"|"+ ''.join(orientation_))
    return edge_lookup_


def get_next_empty_position(grid_):
    for idr, row in enumerate(grid_):
        for idc, col in enumerate(row):
            if grid_[idr][idc] is None:
                return idr, idc


def tids_in_grid(grid_):
    in_grid = []
    for r in grid_:
        for c in [_ for _ in r if _ is not None]:
            in_grid.append(c[0])
    return in_grid


def filter_for_next_pos (neighbour, matching_edge, grid_, tiles_, edge_lookup_):
    if neighbour is None:
        for orientation_ in edge_lookup_:
            for edge_ in edge_lookup_[orientation_]:
                for i in edge_lookup_[orientation_][edge_]:
                    yield i
    else:
        in_grid = tids_in_grid(grid_)
        nid, o = neighbour
        edge_ = rotate_tile(tiles_[nid], (int(o[0]), o[1]))[matching_edge]

        edge_matches = edge_lookup_[(matching_edge+2)%4]
        if edge_ not in edge_matches:
            return []

        for i in edge_matches[edge_]:
            enid, r = i.split("|")
            if enid not in in_grid:
                yield i


def fit_next_tile(grid_, tiles_, edge_lookup_):
    idr, idc = get_next_empty_position(grid_)
    left_neighbour = grid_[idr][idc-1] if idc else None
    top_neighbour = grid_[idr-1][idc] if idr else None

    possible_tiles_matching_top = list(filter_for_next_pos(top_neighbour, 2, grid_, tiles_, edge_lookup_))
    possible_tiles_matching_left = list(filter_for_next_pos(left_neighbour, 1, grid_, tiles_, edge_lookup_))
    possible_tiles = sorted(set(possible_tiles_matching_left).intersection(set(possible_tiles_matching_top)))

    grcp = copy.deepcopy(grid_)
    for idp, possible_tile in enumerate(possible_tiles):
        tid, orientation = possible_tile.split("|")
        grcp[idr][idc] = tid, ''.join(orientation)
        if not (idr == GRID_SIZE-1 and idc == GRID_SIZE-1):
            _ = fit_next_tile(grcp, tiles_, edge_lookup_)

            if _[GRID_SIZE-1][GRID_SIZE-1] is not None:
                return _
    return grcp


# Read input
f = open("ass-day-20-input.txt", "r")
TILE_EDGES_LIB, TILE_FULL_LIB = create_tile_lib(f.read().split("\n\n"))
EDGE_LOOKUP = create_edge_lookup(TILE_EDGES_LIB)
GRID_SIZE = int(math.sqrt(len(TILE_EDGES_LIB)))
TILE_SIZE = len(list(TILE_EDGES_LIB.items())[0][1][0])
print(f"DONE PREPROCESSING. GRID SIZE: {GRID_SIZE}, TILE_SIZE: {TILE_SIZE}")

GRID = []
for c in range(0, GRID_SIZE):
    GRID.append([None] * GRID_SIZE)

# solution = fit_next_tile(GRID, TILE_EDGES_LIB, EDGE_LOOKUP)
solution = [[('1327', '0H'), ('2591', '0.'), ('3623', '2.'), ('2663', '1H'), ('3671', '2.'), ('3011', '0H'), ('1889', '1H'), ('2713', '0H'), ('2861', '2H'), ('1307', '2H'), ('1031', '2H'), ('3571', '2H')], [('1663', '3.'), ('1451', '2H'), ('3467', '1.'), ('1487', '2.'), ('3319', '0.'), ('3637', '1H'), ('3457', '1H'), ('1021', '2.'), ('3673', '1H'), ('1277', '1.'), ('3187', '1.'), ('3823', '1H')], [('3911', '1H'), ('3943', '3.'), ('3191', '0.'), ('2551', '3.'), ('3557', '3.'), ('3917', '0.'), ('2111', '0H'), ('1847', '2.'), ('1231', '2H'), ('2131', '0H'), ('2819', '1H'), ('2311', '3.')], [('1039', '2.'), ('1361', '3.'), ('1693', '1.'), ('2153', '2.'), ('1867', '0.'), ('1931', '2.'), ('1187', '0H'), ('3593', '0H'), ('2707', '2H'), ('1723', '2.'), ('2351', '1.'), ('1747', '0.')], [('2659', '1.'), ('3881', '1.'), ('1699', '2.'), ('3049', '2.'), ('3739', '2.'), ('3037', '1H'), ('1583', '1.'), ('3931', '0H'), ('2027', '2H'), ('1627', '2.'), ('3499', '0.'), ('1787', '1.')], [('2069', '1.'), ('2467', '2H'), ('1831', '1.'), ('2557', '1H'), ('3463', '1.'), ('3793', '0.'), ('1609', '0H'), ('1109', '1.'), ('1409', '0H'), ('1129', '2.'), ('1321', '0.'), ('2957', '2.')], [('3301', '0H'), ('2879', '1.'), ('2719', '0H'), ('2087', '3.'), ('1901', '1H'), ('2447', '0.'), ('3433', '0H'), ('1163', '3.'), ('3733', '1H'), ('3307', '2H'), ('1481', '0.'), ('3677', '1.')], [('3329', '1.'), ('1049', '0H'), ('3833', '2H'), ('3613', '0H'), ('1091', '1.'), ('1613', '1.'), ('1997', '0H'), ('3163', '3.'), ('3251', '3.'), ('3529', '3.'), ('1601', '0H'), ('2473', '3.')], [('1051', '0.'), ('3779', '2H'), ('1993', '1.'), ('3209', '2H'), ('2213', '2.'), ('3709', '2.'), ('2503', '3.'), ('3821', '1.'), ('2531', '1.'), ('3089', '2H'), ('3659', '0.'), ('2609', '2.')], [('2269', '1.'), ('1777', '3.'), ('2297', '2H'), ('2341', '0.'), ('2909', '0.'), ('3167', '2.'), ('1483', '2H'), ('2927', '1.'), ('2687', '1.'), ('1549', '0.'), ('2083', '0H'), ('2339', '0H')], [('1103', '0.'), ('2953', '1.'), ('3079', '3.'), ('3361', '1.'), ('2801', '3.'), ('2647', '1.'), ('1801', '2H'), ('2671', '2.'), ('3061', '0.'), ('3643', '0H'), ('2423', '2.'), ('3221', '2.')], [('3391', '2.'), ('3373', '1.'), ('3323', '0H'), ('1061', '2.'), ('3313', '2H'), ('2689', '1.'), ('2633', '2.'), ('3631', '0H'), ('3181', '2.'), ('2309', '1.'), ('1553', '0H'), ('1823', '0H')]]
print(f"Corner sum= {int(solution[0][0][0]) * int(solution[0][GRID_SIZE - 1][0]) * int(solution[GRID_SIZE - 1][0][0]) * int(solution[GRID_SIZE - 1][GRID_SIZE - 1][0])}")


# Combine everything into one tile
combined_tile = [None] * ((TILE_SIZE - 2) * GRID_SIZE)
for idr, r in enumerate(solution):
    offset = idr*(TILE_SIZE-2)
    for t in r:
        tid, orientation = t
        full_tile = rotate_full_tile(TILE_FULL_LIB[tid], (int(orientation[0]), orientation[1]))
        edgeless_tile = [r[1:-1] for r in full_tile[1:-1]]

        for idx, r in enumerate(edgeless_tile):
            combined_tile[offset + idx] = r if combined_tile[offset + idx] is None else combined_tile[offset + idx] + r


MONSTER = [(0,18), (1,0),(1,5),(1,6), (1,11), (1,12), (1,17), (1,18), (1,19), (2,1), (2, 4), (2,7),(2,10),(2,13), (2,16) ]
MONSTER_LENGTH = 20
MONSTER_HEIGHT = 3

monster_hunt = {}
def find_nr_monsters(combined_tile_):
    for rotation in range(0, 4 ):
        for flip in ['.','H','V']:
            ctile = rotate_full_tile(combined_tile_, (rotation, flip))

            monsters_found = []
            for line_idx, line in enumerate(ctile[:-(MONSTER_HEIGHT-1)]):
                for char_idx, char in enumerate(line[:-(MONSTER_LENGTH-1)]):

                    is_monster = True
                    for i, j in MONSTER:
                        if ctile[line_idx+ i][char_idx + j] != '#':
                            is_monster = False
                            break

                    if is_monster:
                        monsters_found.append((line_idx, char_idx))
                        # print(f"Found monster at ({line_idx},{char_idx})")

            monster_hunt[str(rotation)+flip] = len(monsters_found)

find_nr_monsters(combined_tile)

print(monster_hunt)
max_nr_monsters = max(monster_hunt.values())
print(f"Found max {max_nr_monsters} monsters. Water roughness is {sum([l.count('#') for l in combined_tile]) - max_nr_monsters* 15}")
