#!/usr/bin/env python3

def fakultet(n):
    product = 1
    for number in range(2, n+1):
        product *= number
    return product

print("0! =", fakultet(0))
print("1! =", fakultet(1))
print("5! =", fakultet(5))
print("7! =", fakultet(7))
print("17! =", fakultet(17))
print("361! =", fakultet(361))
