import string

def find_nr_of_containing_bags(bag_color, rules):
    nr_containing_bags = 0

    containing_bags = rules[bag_color]
    for b, cnt in containing_bags:
        nr_containing_bags += (cnt + cnt*find_nr_of_containing_bags(b, rules))

    return nr_containing_bags

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


answer = find_nr_of_containing_bags('shiny gold', rules)

print(answer)


