#!/usr/bin/env python3
import copy

import pretty_print_matrix
"""
3. Skriv en funktion som gör en nxn-enhetsmatris.
"""

def eye(n):
    row_of_zeros = [0] * n
    output_matrix = []
    for i in range(n):
        new_row = copy.copy(row_of_zeros) # row_of_zeros[:] also works
        new_row[i] = 1
        output_matrix.append(new_row)
    return output_matrix

def test_eye():
    assert eye(1) == [[1]]
    assert eye(2) == [[1, 0], [0, 1]]
    assert eye(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    
def show_example_eyes():
    n = 5
    print("eye({}):".format(n))
    #~ print(eye(n))
    pretty_print_matrix.pretty_print_matrix(eye(n))

test_eye()
show_example_eyes()
