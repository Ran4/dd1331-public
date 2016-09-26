

def is_all_positive(seq):
    if not seq:
        return True
    else:
        return seq[0] >= 0 and is_all_positive(seq[1:])
