VERBOSE = True
vprint = print if VERBOSE else lambda *a, **k: None


class CupCircle:
    def __init__(self, cups, current_cup_idx):
        self.cups = cups
        self.cc_idx = current_cup_idx
        self._move_size = 3

    def size(self):
        return len(self.cups)

    def __str__(self):
        s = []
        for idx, cup in enumerate(self.cups):
            s.append('('+str(cup)+')' if idx==self.cc_idx else str(cup))
        return ' '.join(s)

    def _get_pickup(self):
        pickup = []
        for i in range(1, self._move_size + 1):
            idx = (self.cc_idx + i) % self.size()
            pickup.append(self.cups[idx])
        return pickup

    def _get_destination(self, circle):
        cur_label = self.cups[self.cc_idx]
        destination = None

        while not destination and cur_label > 0:
            cur_label -= 1
            if cur_label in circle:
                return circle.index(cur_label)
        return circle.index(max(circle))

    def get_cup(self, idx):
        return self.cups[idx]

    def move(self):
        vprint(f"cups: {self}")

        pickup = self._get_pickup()
        vprint(f"pick up: {', '.join(str(x) for x in pickup)}")

        circle = [_ for _ in self.cups if _ not in pickup]
        dest = self._get_destination(circle)
        vprint(f"destination: {circle[dest]}")

        for cup in pickup:
            dest += 1
            circle.insert(dest, cup)

        '''The crab selects a new current cup: the cup which is immediately clockwise of the current cup.'''
        self.cc_idx = (circle.index(self.cups[self.cc_idx]) + 1) % self.size()
        self.cups = circle


cupcircle = CupCircle([int(i) for i in list('562893147')], 0)
for i in range (1, 101):
    vprint(f"\n-- move {i} --")
    cupcircle.move()

print(f"\n-- final --")
print(f"cups: {cupcircle}")

s = cupcircle.cups.index(1)
output=''
for i in range(1, cupcircle.size()):
    idx = (s+i)%cupcircle.size()
    output += str(cupcircle.get_cup(idx))
print(f'Final output: {output}')

# 38925764