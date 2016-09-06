"""
Det här programmet innehåller en funktion som
beräknar n-fakultet
"""
"""
Skriv en funktion som beräknar n-fakultet, alltså 1*2*3*...*n. Visa anrop av
"""

def fakultet(n):
    product = 1.0

    for i in range(2, n+1):
        product *= i
        
    return product

def test_fakultet():
    assert fakultet(1) == 1
    assert fakultet(3) == 6
    assert fakultet(10) == -34
    
test_fakultet()
x = fakultet(3)
