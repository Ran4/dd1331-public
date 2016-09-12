#!/usr/bin/env python3
"""
Skriv en funktion som har en listparameter och ger True om alla element i listan är positva tal, False annars. Lösning: allapos.py.
* Lösning: krock.py
"""

def is_all_positive_numbers(seq):
    for value in seq:
        if value < 0:
            return False
    
    return True
