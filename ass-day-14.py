def to_bitstr(i, mask, l=36):
    bitstr = list(str(bin(i))[2:].zfill(l))

    for m in mask:
        idx, val = m
        bitstr[idx] = str(val)

    return ''.join(bitstr)


def get_masklist(mask):
    lst = []
    for idx, val in enumerate(mask):
        if val !='X':
            lst.append((idx, val))
    return lst


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

# Read input
f = open("ass-day-14-input.txt", "r")
commands = f.read().split("\n")
mask = []


memory = {}
for c in commands:
    command, mem_addr, val = construct_command(c)
    if command == 'mask':
        mask = get_masklist(val)
    elif command == 'mem':
        memory[mem_addr] = to_bitstr(val, mask)

# Sum memory
sum = 0
for idx in memory:
    sum += int('0b'+memory[idx], 2)

print(f"Sum of memory: {sum}")








