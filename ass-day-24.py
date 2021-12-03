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

# Read input
f = open("ass-day-24-input.txt", "r")

floor = {}
for line in f.read().split("\n"):
    c = str_to_dir(line, 0, 0)
    floor[c] = floor[c] + 1 if c in floor else 1

nr_black = sum(1 for cnt in floor.values() if cnt%2==1)
nr_white = sum(1 for cnt in floor.values() if cnt%2==2)

print(f"Flipped {nr_black+nr_white} tiles, {nr_black} ended up black, {nr_white} ended up white")
#Flipped 275 tiles, 275 ended up black, 0 ended up white
