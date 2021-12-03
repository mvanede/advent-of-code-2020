# Read input
f = open("ass-day-25-input.txt", "r")


def tranform_subject(val_, subject_):
    val_ = val_ * subject_
    return val_ % 20201227

def get_loopsize(key, val_, subject_):
    loopsize = 1
    val_ = tranform_subject(val_, subject_)

    while val_ != key:
        val_ = tranform_subject(val_, subject_)
        loopsize += 1
    return loopsize


def calc_private_key(val_, subject_, loopsize_):
    for i in range(0, loopsize_):
        val_ = tranform_subject(val_, subject_)

    return val_


val = 1
subject = 7
card_pkey = 16616892
door_pkey = 14505727
loopsize_card = get_loopsize(card_pkey, val, subject)
# loopsize_door = get_loopsize(door_pkey, val, subject)
print(f"Card loopsize = {loopsize_card}")

# private_key_card = calc_private_key(val, card_pkey, loopsize_door)
private_key_door = calc_private_key(val, door_pkey, loopsize_card)
print(f"Private_key = {private_key_door}")
#4441893