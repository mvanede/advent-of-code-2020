# Read input
f = open("ass-day-16-input.txt", "r")
fields_txt, my_ticket, nearby_tickets_txt = f.read().split("\n\n")


def parse_valid_values(fields):
    _valid_values = {}
    for field in fields.split("\n"):
        _field_name, values = field.split(": ")

        _valid_values[_field_name] = []
        for value_range in values.split(" or "):
            range_start, range_end = value_range.split("-")
            _valid_values[_field_name] += range(int(range_start), int(range_end)+1)
    return _valid_values


def parse_nearby_tickets(_nearby_tickets_txt):
    tickets = _nearby_tickets_txt.split("\n")[1:]

    _nearby_tickets=[]
    for ticket_values in tickets:
        ticket = [int(n) for n in ticket_values.split(',')]
        _nearby_tickets.append(ticket)

    return _nearby_tickets


nearby_tickets = parse_nearby_tickets(nearby_tickets_txt)
valid_values = parse_valid_values(fields_txt)
all_values = []
for field_name in valid_values:
    all_values += valid_values[field_name]

# Calculate error rate
error_rate = 0
for nb_ticket in nearby_tickets:
    for v in [x for x in nb_ticket if x not in all_values]:
        error_rate += v


print(f"Scanning done. Error rate: {error_rate}")