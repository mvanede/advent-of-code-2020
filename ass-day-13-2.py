
# Read input
f = open("ass-day-13-input.txt", "r")
notes = f.read().split("\n")
earliest_departure = int(notes[0])
busses = [b for b in notes[1].split(',')]


def next_match(start, delta, increase_step, bus_id2):
    i = start
    while True:
        if (i+delta)%bus_id2 == 0:
            return i
        i += increase_step


first_bus = int(busses[0])
other_busses = []
for idx, bus in enumerate(busses):
    if bus != 'x' and idx != 0:
        other_busses.append((idx, int(bus)))


increase_step = first_bus
start_time = 0
for delta, bus_id  in other_busses:
    i = next_match(start_time, delta, increase_step, bus_id)
    increase_step *= bus_id
    start_time = i

print(f"Found matching departure time: {i}")
