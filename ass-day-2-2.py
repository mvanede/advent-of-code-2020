def is_valid(min, max, letter, password):
    x = password[min-1] == letter
    y = password[max-1] == letter
    return x != y

f = open("ass-day-2-input.txt", "r")
lines = f.read().split("\n")
passwords = [line.split(" ") for line in lines]

correct_passwords = 0
for p in passwords:
    min, max = map(int, p[0].split("-"))
    if is_valid(min, max, p[1][:1], p[2]):
        correct_passwords+=1

print (correct_passwords)