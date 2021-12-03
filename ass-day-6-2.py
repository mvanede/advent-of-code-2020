import string

def get_nr_answers(group):
    overlap = set(string.ascii_lowercase)

    for p in group:
        overlap = overlap.intersection(set(p))

    return len(overlap)

# Read field
f = open("ass-day-6-input.txt", "r")
lines = f.read().split("\n\n")
groups = [line.split("\n") for line in lines]


nr_answers = 0
for group in groups:
    nr_answers += get_nr_answers(group)

print(nr_answers)