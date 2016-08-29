#!/usr/bin/env python3
print("Det här programmet beräknar N när summan av 1/i, i = 1..N nått ett visst mål")
target_sum = float(input("Vilken summa vill du uppnå? "))

term_counter = 0
sum_ = 0
while sum_ < target_sum:
    term_counter += 1
    sum_ += 1 / term_counter
    
print("Med", term_counter, "termer blir summan", sum_)
