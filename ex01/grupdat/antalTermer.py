#coding:latin1

limit = float(input("Vilken summa vill du uppnå? "))

n = 0
sum = 0
while sum < limit:
    n += 1
    sum += 1/n

print("Med",n,"termer blir summan",sum)
