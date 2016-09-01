#coding:latin1

n = int(input("Hur många termer? "))

k = 0
sum = 0
while k<n:
    k += 1
    sum += 1/k

print("Summan av",n,"termer =",sum)
