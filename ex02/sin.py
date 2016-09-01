# coding: latin1

import math

def taylorsin(x):
    sum = term = x
    eps = 1e-10            # lite godtyckligt vald gräns
    k = 1                  
    sign = 1               # termens tecken, alternerar mellan +1 och -1
    while abs(term) >eps:  # summera sa länge som nästa term > eps
        k += 2
        sign = -sign 
        term = term*x*x/(k-1)/k  # nästa term beräknas ur föregående
        sum += sign*term
    return sum


# Har testas funktionen med några anrop
# Värdet av math.sin() skrivs ut for jämförelse 

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
