import math
import copy


def create_tile_lib(tiles_txt):
    tile_lib = {}
    for tile in tiles_txt:
        t = tile.split("\n")
        tid = t[0][5:-1]
        tile_lib[tid] = [t[1:][0], ''.join([x[-1:] for x in t[1:]]), t[1:][-1:][0], ''.join([x[:1] for x in t[1:]])]
    return tile_lib


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
    possible_tiles = set(possible_tiles_matching_left).intersection(set(possible_tiles_matching_top))

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
TILE_LIB = create_tile_lib(f.read().split("\n\n"))
EDGE_LOOKUP = create_edge_lookup(TILE_LIB)
GRID_SIZE = int(math.sqrt(len(TILE_LIB)))
print(f"DONE PREPROCESSING. GRID SIZE: {GRID_SIZE}")

GRID = []
for c in range(0, GRID_SIZE):
    GRID.append([None] * GRID_SIZE)

solution = fit_next_tile(GRID, TILE_LIB, EDGE_LOOKUP)
print(f"Corners = {solution[0][0][0]}, {solution[0][GRID_SIZE - 1][0]} - {solution[GRID_SIZE - 1][0][0]} - {solution[GRID_SIZE - 1][GRID_SIZE - 1][0]}")
print(f"Corner sum= {int(solution[0][0][0]) * int(solution[0][GRID_SIZE - 1][0]) * int(solution[GRID_SIZE - 1][0][0]) * int(solution[GRID_SIZE - 1][GRID_SIZE - 1][0])}")
