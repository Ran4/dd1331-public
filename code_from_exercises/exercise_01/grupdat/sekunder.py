#coding:latin1

sekunder = int(input("Hur många sekunder? "))

sek = sekunder % 60
min = (sekunder//60) % 60
tim = (sekunder//60//60) % 24
dag = (sekunder//60//60//24)

print("Det blir",dag,"dagar,",tim,"timmar, ",min,"minuter och", sek, "sekunder")


'''
Om man tycker det är onödigt att göra samma division flera 
gånger så kan man lösa uppgiften så här:

restv = int(input("Hur många sekunder? "))

restv = sekunder
sek = restv % 60
restv //= 60
min = restv % 60
restv //= 60
tim = restv % 24
dag = restv // 24

print("Det blir",dag,"dagar,",tim,"timmar, ",min,"minuter och", sek, "sekunder")

'''
