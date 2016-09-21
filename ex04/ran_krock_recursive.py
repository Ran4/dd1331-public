#!/usr/bin/env python3
"""
Skriv en funktion som --med hjälp av rekursion-- tar en listparameter och ger
True om alla element i listan är positiva tal, False annars.
"""

def is_all_positive_numbers(seq):
    if len(seq) == 0:
        return True
    return seq[0] >= 0 and is_all_positive_numbers(seq[1:])

def test_is_all_positive_numbers_recursive():
    assert is_all_positive_numbers([3, 4, 5]) == True
    assert is_all_positive_numbers([4, 3, 5]) == True
    assert is_all_positive_numbers([3, 4, 5]) == True
    assert is_all_positive_numbers([3, -4, 5]) == False
    
test_is_all_positive_numbers_recursive()
