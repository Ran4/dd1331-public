#!/usr/bin/env python3
import math
"""
3. Pythonkramaren, uppgift 25: Beräkna siffersumman för ett tresiffrigt heltal.
Exempel: siffersumman av 413 är 4 + 1 + 3 = 8.
Lösning: [siffer3summa.py](siffer3summa.py).
"""

number = int(input("Skriv in ett tresiffrigt tal: "))

if number > 1000:
    print("För stort!")
elif number < 0:
    print("För litet!")
else:
    first_digit = (number // 1) % 10
    second_digit = (number // 10) % 10
    third_digit = (number // 100) % 10
    
    digit_sum = first_digit + second_digit + third_digit
    
    print("The digit sum of {}, {} and {} is {}".format(
        third_digit, second_digit, first_digit, digit_sum))
