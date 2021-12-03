def calc(l, sum_of):
    for idx, val in enumerate(l):
        for val2 in l[idx + 1:]:
            for val3 in l[idx + 2:]:
                s = val + val2 + val3
                if s == sum_of:
                    return val * val2 * val3


f = open("ass-day-1-input.txt", "r")
lines = f.read().split("\n")
numbers = [int(line) for line in lines]

print(calc(numbers, 2020))
