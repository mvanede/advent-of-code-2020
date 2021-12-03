
# Read field
f = open("ass-day-4-input.txt", "r")
lines = f.read().split("\n\n")
pl = [line.split() for line in lines]
passports = [dict((k[:3], k[4:]) for k in p) for p in pl]

def is_valid(passport, required_keys):
    keys = list(passport.keys())
    return all(elem in keys for elem in required_keys)

cnt=0
for passport in passports:
    if is_valid(passport, ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
        cnt += 1

print(cnt)