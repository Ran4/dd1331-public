#coding:latin1
print("Skriv sidl�ngderna f�r din triangel: ", end = "")
a = int(input())
b = int(input())
c = int(input())

if a < b+c and b < c+a and c < a+b:
    s = (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Ytan �r",A)
else:
    print("De sidl�ngderna kan inte bilda triangel!")
