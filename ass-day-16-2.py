def parse_valid_values(fields):
    _valid_values = {}
    for _field in fields.split("\n"):
        _field_name, values = _field.split(": ")

        _valid_values[_field_name] = []
        for value_range in values.split(" or "):
            range_start, range_end = value_range.split("-")
            _valid_values[_field_name] += range(int(range_start), int(range_end)+1)
    return _valid_values


def parse_nearby_tickets(nearby_tickets_txt):
    tickets = nearby_tickets_txt.split("\n")[1:]

    _nearby_tickets=[]
    for ticket_values in tickets:
        _ticket = [int(n) for n in ticket_values.split(',')]
        _nearby_tickets.append(_ticket)

    return _nearby_tickets


# Read input
f = open("ass-day-16-input.txt", "r")
fields_txt, my_ticket_txt, nearby_tickets_txt = f.read().split("\n\n")

# Parse blocks
nearby_tickets = parse_nearby_tickets(nearby_tickets_txt)
my_ticket = parse_nearby_tickets(my_ticket_txt)[0]
valid_values = parse_valid_values(fields_txt)

# Combine all valid values for all fields as a helper
all_values = []
for field_name in valid_values:
    all_values += valid_values[field_name]

# Remove all invalid tickets
valid_nearby_tickets = []
for nb_ticket in nearby_tickets:
    if len([x for x in nb_ticket if x not in all_values])==0:
        valid_nearby_tickets.append(nb_ticket)


# Fill tmp array for determination, determine possible fields for each value on each ticket
field_determination = [list(valid_values.keys()) for i in valid_nearby_tickets[0]]
for ticket in valid_nearby_tickets:
    for idx, v in enumerate(ticket):
        for field_name in valid_values:
            if not v in valid_values[field_name]:
                field_determination[idx].remove(field_name)


# Assuming valid input; order on length and remove duplicates. Making use of references, instead of deepcopy
ordered_fields = field_determination.copy()
ordered_fields.sort(key=len)
for idx, lst in enumerate(ordered_fields):
    r = lst[0]
    for lst2 in ordered_fields[idx+1:]:
        lst2.remove(r)

# Calculate checksum
checksum = 1
for idx, field in enumerate(field_determination):
    if field[0][:9] == 'departure':
        checksum *= my_ticket[idx]

print(f"Scanning done. checksum: {checksum}")