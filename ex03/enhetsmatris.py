import copy
"""
3. Skriv en funktion som gör en N x N-enhetsmatris.
"""

def eye(n=0):
    rows = []
    zero_row = [0] * n
    
    for i in range(n):
        new_row = zero_row[:]
        new_row = copy.copy(zero_row)
        new_row[i] = 1
        rows.append(new_row)

    return rows

def test_eye():
    assert eye() == []
    assert eye(1) == [[1]]
    assert eye(2) == [[1, 0], [0, 1]]
    assert eye(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("All tests finished successfully! Yay!")
    
test_eye()
