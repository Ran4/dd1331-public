"""
Beräkna siffersumman för ett tresiffrigt heltal.
Exempel: Siffersumman av 413 är 4 + 1 + 3 = 8
"""

number = int(input("Skriv in ditt tal "))

if number < 0:
    print("Ditt tal är inte positivt!")
    exit()
elif number > 1000:
    print("Ditt tal är större än 1000")
    exit()

first_digit = number % 10
second_digit = (number // 10) % 10
third_digit = number // 100

digit_sum = first_digit + second_digit + third_digit

print("Siffersumman är:", digit_sum)
