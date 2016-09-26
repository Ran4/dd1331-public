


def is_ordered(seq):
    if len(seq) >= 2:
        return seq[0] <= seq[1] and is_ordered(seq[2:])
    else:
        return True
