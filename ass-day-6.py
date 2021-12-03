import string


def get_nr_answers(group):
    alphabet = set(string.ascii_lowercase)

    combined = set()
    for p in group:
        overlap = alphabet.intersection(set(p))
        combined.update(overlap)

    return len(combined)

# Read field
f = open("ass-day-6-input.txt", "r")
lines = f.read().split("\n\n")
groups = [line.split("\n") for line in lines]


nr_answers = 0
for group in groups:
    nr_answers += get_nr_answers(group)

print(nr_answers)