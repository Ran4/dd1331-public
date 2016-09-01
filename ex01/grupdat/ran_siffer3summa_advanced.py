#!/usr/bin/env python3
import math
"""
3. Pythonkramaren, uppgift 25: Beräkna siffersumman för ett tresiffrigt heltal.
Exempel: siffersumman av 413 är 4 + 1 + 3 = 8.
Lösning: [siffer3summa.py](siffer3summa.py).
"""

def get_siffersumma_info_string(number):
    if number > 1000:
        return "För stort!"
    elif number < 0:
        return "För litet!"
    else:
        first_digit = (number // 1) % 10
        second_digit = (number // 10) % 10
        third_digit = (number // 100) % 10
        
        digit_sum = first_digit + second_digit + third_digit
        
        return "The digit sum of {}, {} and {} is {}".format(
            third_digit, second_digit, first_digit, digit_sum)
        
def get_valid_number_or_exit():
    raw_number = input("Skriv in ett tresiffrigt tal: ")
    try:
        number = int(raw_number)
    except ValueError:
        print("Invalid input")
        exit()
    return number

number = get_valid_number_or_exit()
print(get_siffersumma_info_string(number))
