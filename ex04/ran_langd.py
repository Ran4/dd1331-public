

def length(seq):
    if not seq:
        return 0
    return 1 + length(seq[1:])

