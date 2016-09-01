# coding: latin1

import math

def taylorsin(x):
    sum = term = x
    eps = 1e-10            # lite godtyckligt vald gr�ns
    k = 1                  
    sign = 1               # termens tecken, alternerar mellan +1 och -1
    while abs(term) >eps:  # summera sa l�nge som n�sta term > eps
        k += 2
        sign = -sign 
        term = term*x*x/(k-1)/k  # n�sta term ber�knas ur f�reg�ende
        sum += sign*term
    return sum


# Har testas funktionen med n�gra anrop
# V�rdet av math.sin() skrivs ut for j�mf�relse 

t = 0.37
print("t= ", t)
print(taylorsin(t))
print(math.sin(t))
print()

t = 2.16
print("t= ", t)
print(taylorsin(t))
print(math.sin(t))
print()
