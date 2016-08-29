#!/usr/bin/env python3
print("Det här programmet beräknar summan av 1/i, i = 1..N")
num_terms = int(input("Hur många termer (=N)? "))

term_counter = 0
sum_ = 0
while term_counter < num_terms:
    term_counter += 1
    sum_ += 1 / term_counter
    
print("Summan av", num_terms, "termer =", sum_)
