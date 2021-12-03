import string

def find_containing_bags(bag_color, rules):
    can_be_contained_in = set()

    for containing_bag, contains in rules.items():
        if bag_color in ([i[0] for i in contains]):
            can_be_contained_in.add(containing_bag)

    if len(can_be_contained_in) > 0:
        for c in can_be_contained_in.copy():
            can_be_contained_in = can_be_contained_in.union(find_containing_bags(c, rules))

    return can_be_contained_in

# Read field
f = open("ass-day-7-input.txt", "r")
lines = f.read().split("\n")
rules = {}
for line in lines:
    x,y = line.split("contain")
    key = " ".join(x.split(" ")[:2])

    contain_list = []
    if not 'no other bags' in y:
        contains_bags = y.split(', ')
        for c in contains_bags:
            parts = c.strip().split(' ')
            amount = int(parts[0])
            c_key = " ".join([parts[1], parts[2]])
            contain_list.append((c_key, amount))

    rules[key] = contain_list

answer = find_containing_bags('shiny gold', rules)
print(answer)
print(len(answer))

