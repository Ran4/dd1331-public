"""
1. Pythonkramaren 63: Skriv en funktion som tar en listparameter och ger True om alla element i listan är positiva tal, False annars.
"""

def is_all_number_positive(seq):
    for number in seq:
        if number < 0:
            return False
    
    return True
