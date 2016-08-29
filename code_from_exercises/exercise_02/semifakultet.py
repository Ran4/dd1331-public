# coding: latin1

def semifak(n):
    p = 1
    for k in range(n,1,-2):    # Gå från n med steg -2 ned till 1
        p *= k                 # Sista värdet som används kommer
                               # att vara 3 (udda n) eller 2 (jämnt n)
    return p                   # Repetitionen stannar innan gränsen nås


# Testa med några anrop

print('0!! =', semifak(0))
print('1!! =', semifak(1))
print('5!! =', semifak(5))
print('8!! =', semifak(8))


'''
Har ar en alternativ definition som anvander while

def semifak(n):
    p = 1
    k = n
    while k > 1:
        p *= k
        k -= 2

    return p
'''
