
def euklides(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a


# Tester

a = 32*7*7*3*3697
b = 7*7*11*13*3*17*19
print(a,b,euklides(a,b))
print(b,a,euklides(b,a))

a = 3697
b = 11
print(a,b,euklides(a,b))
print(b,a,euklides(b,a))



