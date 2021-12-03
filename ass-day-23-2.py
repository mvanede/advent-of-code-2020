VERBOSE = False
vprint = print if VERBOSE else lambda *a, **k: None


class Cup:
    def __init__(self, val, prv, nxt):
        self.val = val
        self.prv = prv
        self.nxt = nxt

    def __str__(self):
        return f"({self.prv.val}) - <{self.val}> - ({self.nxt.val})"


class CupCircle:
    _move_size = 3

    def __init__(self, input_, current_cup_idx):
        prv = first_cup = Cup(input_[0], None, None)
        self.maxval = input_[0]
        self.cc = prv if current_cup_idx == 0 else None
        self.lbl_index = {first_cup.val: first_cup}

        for idx, val in enumerate(input[1:]):
            prv.nxt = Cup(val, prv, None)
            self.lbl_index[val] = prv.nxt

            if current_cup_idx == (idx + 1):
                self.cc = prv.nxt

            if val > self.maxval:
                self.maxval = val
            prv = prv.nxt

        # Close the chain
        prv.nxt = first_cup
        first_cup.prv = prv

    def get_cup_with_label(self,label):
        return self.lbl_index[label]

    def _get_pickup(self):
        nxt_ = self.cc.nxt
        for i in range(0, self._move_size):
            yield nxt_
            nxt_ = nxt_.nxt

    def _get_destination(self, excluded):
        cur_label = self.cc.val

        while cur_label > 1:
            cur_label -= 1
            if cur_label not in excluded:
                return self.lbl_index[cur_label]

        mx = self.maxval
        while mx in excluded:
            mx -= 1
        return self.get_cup_with_label(mx)


    def move(self):
        pickup_cups = list(self._get_pickup())
        # vprint(f"pick up: {', '.join(str(x.val) for x in pickup_cups)}")

        dest = self._get_destination(excluded=[x.val for x in pickup_cups])
        # vprint(f"destination: {dest.val}")

        for cup in pickup_cups:
            # Unlink cup: make the next of the previous cup the next of this cup
            cup.prv.nxt = cup.nxt
            cup.nxt.prv = cup.prv

            # Insert after dest
            dest.nxt.prv = cup
            cup.nxt = dest.nxt

            dest.nxt = cup
            cup.prv = dest
            dest = cup

        '''The crab selects a new current cup: the cup which is immediately clockwise of the current cup.'''
        self.cc = self.cc.nxt

    def __str__(self):
        circle_lst = [f'({str(self.cc.val)})']
        nxt_ = self.cc.nxt

        while nxt_ is not self.cc:
            circle_lst.append(str(nxt_.val))
            nxt_ = nxt_.nxt

        return ' '.join(circle_lst)


input = [int(i) for i in list('562893147')] + [i for i in range(10, 1_000_001)]
circle = CupCircle(input, 0)

for i in range(1, 10_000_001):
    circle.move()
    if i%100000 == 0:
        print(f"\n-- move {i} --")

print(f"\n-- final --")
s = circle.get_cup_with_label(1)
s1 = s.nxt
s2 = s1.nxt
print(f'Final output: {s1.val * s2.val}')
# 131152940564


# s = circle.get_cup_with_label(1)
# output=''
# nxt = s.nxt
# while nxt is not s:
#     output += str(nxt.val)
#     nxt = nxt.nxt
# print(f'Final output: {output}')
# 38925764
