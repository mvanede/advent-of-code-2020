
# Read input
f = open("ass-day-13-input.txt", "r")
notes = f.read().split("\n")

earliest_departure = int(notes[0])
busses = [int(b) for b in notes[1].split(',') if b != 'x']
print(busses)

def find_first_bus(earliest_departure, busses):

    i = earliest_departure
    while True:
        for bus in busses:
            if i%bus == 0:
                return bus, i
        i +=1


bus_id, departure_time = find_first_bus(earliest_departure, busses)

waiting_time = departure_time-earliest_departure
print(f"Found bus {bus_id}, departs at {departure_time}, waiting time {waiting_time}, multiplied={waiting_time*bus_id}")
