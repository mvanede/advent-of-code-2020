def parse_parentheses(string):
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield len(stack), string[start + 1: i]


# Always number, operator, number, etc
def calculate_simple_expression(input_):
    parts = input_.split(' ')
    _sum = int(parts[0])
    operator = None
    for idx, p in enumerate(parts[1:]):
        if idx%2:
            if operator == '+':
                _sum += int(p)
            elif operator == '*':
                _sum *= int(p)
        else:
            operator = p
    return _sum


def calc(_input):
    stack = {}
    for e in parse_parentheses('(' + _input + ')'):
        depth, expression = e

        if not '(' in expression:
            _sum = calculate_simple_expression(expression)
        else:
            for k in stack:
                expression = expression.replace(k, str(stack[k]))
            _sum = calculate_simple_expression(expression)

        stack['(' + expression + ')'] = _sum
    return _sum


# Read input
f = open("ass-day-18-input.txt", "r")
lines = f.read().split("\n")
my_sum = 0
for line in lines:
    my_sum += calc(line)

print(f"Sum of all: {my_sum}")

