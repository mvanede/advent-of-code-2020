
# Read field
f = open("ass-day-3-input.txt", "r")
lines = f.read().split("\n")
field = [list(line) for line in lines]

def count_trees(x_diff, y_diff):
    x,y = 0,0
    tree_count=0
    while y<len(lines):
        x = x%len(field[y])
        if field[y][x] =='#':
            tree_count+=1
        x +=x_diff
        y += y_diff
    return tree_count

print(count_trees(3,1))