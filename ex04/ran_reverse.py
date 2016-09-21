

def recursive_reverse(seq):
    if len(seq) > 1:
        head, tail = seq[0], seq[1:]
        return recursive_reverse(tail) + [head]
    
    return seq

print(recursive_reverse([3, 4, 5]))
