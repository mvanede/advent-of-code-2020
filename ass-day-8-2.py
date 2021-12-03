
def execute_program(program):
    executed = []
    accumulator, index = 0,0

    finished_program = False
    try:
        while index not in executed:
            executed.append(index)
            linenr, oper, val = program[index]
            if oper=='acc':
                accumulator += val
                index += 1
            elif oper=='nop':
                index += 1
            elif oper=='jmp':
                index += val
    except IndexError as e:
        finished_program = True

    finally:
        return finished_program, accumulator


# Read program
f = open("ass-day-8-input.txt", "r")
lines = f.read().split("\n")

program = []
for idx, line in enumerate(lines):
    x,y = line.split(" ")
    program.append((idx, x, int(y)))

jmp_nop = filter(lambda c: c[1] in('jmp','nop'), program)
for linenr, oper, val in list(jmp_nop):
    program_c = program.copy()
    program_c[linenr] = (linenr, 'jmp' if oper == 'nop' else 'nop', val)
    program_reached_end, accumulator = execute_program(program_c)

    if program_reached_end:
        print("REACHED THE END: " + str(accumulator))
        break
    else:
        continue