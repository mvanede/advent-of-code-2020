def get_partition(sequence, lower_half='F', nr_of_rows=128):
    partition = list(range(0,nr_of_rows))
    for p in sequence:
        i = int(len(partition) / 2)
        partition = partition[:i] if p==lower_half else partition[-i:]

    return partition[0]

def get_seat(sequence, nr_of_rows=128, nr_of_seats=8):
    return (get_partition(sequence[:7], 'F', nr_of_rows), get_partition(sequence[-3:], 'L', nr_of_seats))

def get_seat_id(row, seat):
    return row*8 + seat


# Read field
f = open("ass-day-5-input.txt", "r")
sequences = f.read().split("\n")

seats = []
for seq in sequences:
    row, seat = get_seat(seq)
    seats.append(get_seat_id(row, seat))

all = list(range(8, 977))
print(set(all)-set(seats))
