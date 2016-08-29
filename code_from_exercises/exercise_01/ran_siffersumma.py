#!/usr/bin/env python3
number = int(input("Skriv in ett tresiffrigt tal: "))

if number > 1000:
    print("För stort!")
    exit()

digit_sum = 0
while number > 0:
    digit = number % 10
    digit_sum += digit
    
    number //= 10
    
print("Summa:", digit_sum)
