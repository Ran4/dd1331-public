#!/usr/bin/env python3

description_text = "Skriv in ett antal tal. Avsluta med enter"
print(description_text)

sum_ = 0
num_numbers = 0
while True:
    raw_input = input("> ")
    
    if raw_input == "":
        break
    
    number = float(raw_input)
    sum_ += number
    num_numbers += 1
    
average = sum_ / num_numbers
rounded_average = round(sum_ / num_numbers, 2)
    
print("Medelvärdet av dina {} tal är {}".format(
    num_numbers, rounded_average))
