def parse_parentheses(string):
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield len(stack), string[start + 1: i]


def sum_up(input_):
    to_sum = [int(n) for n in input_.split(' + ')]
    return sum(to_sum)


def calculate_simple_expression(input_):
    parts = input_.split(' * ')
    _sum = 1
    for idx, expr in enumerate(parts):
        val = sum_up(expr) if '+' in expr else int(expr)
        _sum *= val
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

