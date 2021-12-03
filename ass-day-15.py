# Read input
f = open("ass-day-15-input.txt", "r")
starting_numbers = [int(n) for n in f.read().split(",")]


history = {}
previously_spoken = [-1]
for i in range(1,30000001):
    prev = previously_spoken[-1]

    if i <= len(starting_numbers):
        turn = starting_numbers[i-1]
    else:
        if prev in history and history[prev]['count'] == 1:
            turn = 0
        elif prev in history and history[prev]['count'] > 0:
            turn = history[prev]['last'][1] - history[prev]['last'][0]

    if i%100000 == 0:
        print(f"Turn {i} = {turn}")

    if turn not in history:
        x = {'count': 1, 'last': [0,i]}
    else:
        x = history[turn]
        x['count'] += 1
        x['last'].append(i)
        x['last'] = x['last'][-2:]

    history[turn] = x
    previously_spoken.append(turn)
    previously_spoken = previously_spoken[-10:]

print(f"Turn {i} = {turn}")