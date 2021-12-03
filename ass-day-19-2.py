import re
from pprint import pprint

VERBOSE = True
vprint = print if VERBOSE else lambda *a, **k: None

def parse_to_ruleset(rules_txt_):
    ruleset = {}
    for rline in rules_txt_.split("\n"):
        id, rule = rline.split(': ')

        if id == '8':
            rule = '42 | 42 8'

        if id == '11':
            rule = '42 31 | 42 11 31'

        if '"' in rule:
            ruleset[int(id)] = rule.replace('"','')
        else:
            possibilities = []
            for p in rule.split(' | '):
                a = p.replace('"','') if '"' in p else [int(x) for x in p.split(' ')]
                possibilities.append(a)

            ruleset[int(id)] = possibilities if len(possibilities)>1 else possibilities[0]
    return ruleset


# recursief vervangen
REGEXP_PER_ID = {}
def get_regexp(rule_id, ruleset, recursion_depth):
    global REGEXP_PER_ID
    rule = ruleset[rule_id]
    if recursion_depth == 30:
        return ''

    if type(rule) is str:
        rval = rule

    elif type(rule[0]) is list:
        or_expr = []
        for r in rule:

            and_expr = []
            for r_id in r:
                # add recursion for OR rules (quick n dirty, works for this ruleset)
               and_expr.append(get_regexp(r_id, ruleset, recursion_depth+1))
            or_expr.append('('+''.join(and_expr)+')')

        rval = '(' + '|'.join(or_expr) + ')'
    else:
        and_expr = []
        for r_id in rule:
            and_expr.append (get_regexp(r_id, ruleset, recursion_depth))
        rval = '('+''.join(and_expr)+')'

    REGEXP_PER_ID[rule_id] = rval
    return rval


# Read input
f = open("ass-day-19-input.txt", "r")
rules_txt, messages_txt = f.read().split("\n\n")
ruleset = parse_to_ruleset(rules_txt)
regexp = get_regexp(0, ruleset, 0)

pprint(REGEXP_PER_ID)



messages = messages_txt.split('\n')
messages.sort()

pattern = re.compile(regexp)
matching = 0
for message in messages:
    if re.fullmatch(pattern, message):
        vprint(f"{message}: OK")
        matching += 1
    else:
        vprint(f"{message}: NOK")

print(f"Done. Found {matching} matching strings")
