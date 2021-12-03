def to_bitstr(i, l=36):
    return str(bin(i))[2:].zfill(l)


def to_int(bitstr):
    return int('0b'+bitstr, 2)


def apply_mask(bitstr, mask):
    b = list(bitstr)

    for m in get_masklist(mask):
        idx, val = m
        if val != '0':
            b[idx] = str(val)

    return ''.join(b)


def get_masklist(mask):
    lst = []
    for idx, val in enumerate(mask):
        lst.append((idx, val))
    return lst


def get_floating_possibilities(mask):
    first_char = mask[0]

    if first_char == 'X':
        results = ['1', '0']
    else:
        results = [first_char]

    if len(mask) > 1:
        combinations = []
        for m in get_floating_possibilities(mask[1:]):
            for r in results:
                combinations.append(r + m)
        return combinations
    else:
        return results

def construct_command(command):
    if command[:3] == 'mem':
        mem, val = command.split(' = ')
        mem_addr = mem[4:][:-1]
        return 'mem', int(mem_addr), int(val)
    elif command[:4] == 'mask':
        mem, val = command.split(' = ')
        return 'mask', 0, val
    else:
        print(f"Unknown command: {command}")


def write_to_mem(memory, mem_addr, mask, val):
    masked = apply_mask(to_bitstr(mem_addr), mask)

    for x in get_floating_possibilities(masked):
        memidx = to_int(x)
        memory[memidx] = val


# Read input
f = open("ass-day-14-input.txt", "r")
commands = f.read().split("\n")
mask = ''

memory = {}
for c in commands:
    command, mem_addr, val = construct_command(c)
    if command == 'mask':
        mask = val
    elif command == 'mem':
        write_to_mem(memory, mem_addr, mask, val)

# Sum memory
sum = 0
for idx in memory:
    sum += memory[idx]

print(f"Sum of memory: {sum}")