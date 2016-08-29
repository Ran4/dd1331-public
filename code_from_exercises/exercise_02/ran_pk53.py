#!/usr/bin/env python3
"""
6. Pythonkramaren 53: funktion som avgör från ett personnummer om ett nummer är manligt eller kvinnligt. Lösning:  pk53.py.

"""

def is_female(personal_number_string):
    """Given a personal number with the format "yymmdd-ssss", returns
    True if it belongs to a female, else False.
    
    Example:
    >>> is_female("920508-0329")
    False
    >>> is_female("920508-0022")
    True
    """
    digit_string = personal_number_string[-1]
    digit = int(digit_string)
    if digit % 2 == 0: #even digit
        return True
    else:
        return False
    
def test_is_female():
    assert is_female('yymmdd-0022')
    assert is_female('yymmdd-0110')
    assert is_female('yymmdd-1458')
    assert is_female('yymmdd-0312')
    assert not is_female('yymmdd-0127')
    
test_is_female()
    
print('Mamma', is_female('yymmdd-0022'))
print('Pappa', is_female('yymmdd-1458'))
print('Lillasyster', is_female('yymmdd-0127'))
print('Lillebror', is_female('yymmdd-0110'))
print('Storebror', is_female('yymmdd-0312'))
