import string

# Read field
f = open("ass-day-8-input.txt", "r")
lines = f.read().split("\n")

program = []
for idx, line in enumerate(lines):
    x,y = line.split(" ")
    program.append((idx, x, int(y)))


def execute_program(program):
    executed = []
    accumulator = 0
    index = 0

    end_reached = False
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
        end_reached = True

    finally:
        return end_reached, accumulator


end_reached, accumulator = execute_program(program)


if end_reached:
    print("REACHED THE END!")
else:
    print("DUPLICATE OPER")

print(accumulator)
