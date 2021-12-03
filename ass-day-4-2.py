import re
# Read field
f = open("ass-day-4-input.txt", "r")
lines = f.read().split("\n\n")
pl = [line.split() for line in lines]
passports = [dict((k[:3], k[4:]) for k in p) for p in pl]


def is_valid_byr(val):
    return int(val) in range(1920, 2002 + 1)


def is_valid_iyr(val):
    return int(val) in range(2010, 2020 + 1)


def is_valid_eyr(val):
    return int(val) in range(2020, 2030 + 1)

def is_valid_hgt(val):
    unit = val[-2:]
    return unit=='cm' and  int(val[:-2]) in range(150, 193 + 1) \
            or unit=='in' and  int(val[:-2]) in range(59, 76 + 1)


def is_valid_hcl(val):
    p = re.compile('\#[0-9a-f]{6}')
    return p.match(val) is not None


def is_valid_ecl(val):
    return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_pid(val):
    p = re.compile('^[0-9]{9}$')
    return p.match(val) is not None

def is_valid(passport, required_keys):
    keys = list(passport.keys())
    if not all(elem in keys for elem in required_keys):
        return False

    return is_valid_byr(passport['byr']) \
            and is_valid_iyr(passport['iyr']) \
            and is_valid_eyr(passport['eyr']) \
            and is_valid_hgt(passport['hgt']) \
            and is_valid_hcl(passport['hcl']) \
            and is_valid_ecl(passport['ecl']) \
            and is_valid_pid(passport['pid'])


    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''


cnt=0
for passport in passports:
    if is_valid(passport, ['byr','iyr','eyr','hgt','hcl','ecl','pid']):
        cnt += 1

print(cnt)