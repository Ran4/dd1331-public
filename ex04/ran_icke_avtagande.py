

def is_sorted(seq):
    """Returns True if all elements in seq is in order,
    e.g. seq[i] <= seq[i+1] for each element i = 0..len(seq) exclusive
    """
    if len(seq) >= 2:
        return seq[0] <= seq[1] and is_sorted(seq[1:])
    else:
        return True
    
def test_is_sorted():
    assert is_sorted([3, 4, 5]) == True
    assert is_sorted([3, 3, 3]) == True
    assert is_sorted([4, 3, 5]) == False
    assert is_sorted([-4]) == True
    assert is_sorted([]) == True
    
test_is_sorted()
