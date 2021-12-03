import re

VERBOSE = True
vprint = print if VERBOSE else lambda *a, **k: None

def parse_to_ruleset(rules_txt_):
    ruleset = {}
    for rline in rules_txt_.split("\n"):
        id, rule = rline.split(': ')

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
def get_regexp(rule_id, ruleset):
    rule = ruleset[rule_id]
    if type(rule) is str:
        return rule

    if type(rule[0]) is list:
        or_expr = []
        for r in rule:
            and_expr = []
            for r_id in r:
                and_expr.append(get_regexp(r_id, ruleset))
            or_expr.append('('+''.join(and_expr)+')')

        return '(' + '|'.join(or_expr) + ')'
    else:
        and_expr = []
        for r_id in rule:
            and_expr.append (get_regexp(r_id, ruleset))
        return '('+''.join(and_expr)+')'



# Read input
f = open("ass-day-19-input.txt", "r")
rules_txt, messages_txt = f.read().split("\n\n")
ruleset = parse_to_ruleset(rules_txt)
regexp = get_regexp(0, ruleset)

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
