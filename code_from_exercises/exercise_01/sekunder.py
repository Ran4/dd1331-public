#coding:latin1

sekunder = int(input("Hur m�nga sekunder? "))

sek = sekunder % 60
min = (sekunder//60) % 60
tim = (sekunder//60//60) % 24
dag = (sekunder//60//60//24)

print("Det blir",dag,"dagar,",tim,"timmar, ",min,"minuter och", sek, "sekunder")


'''
Om man tycker det �r on�digt att g�ra samma division flera 
g�nger s� kan man l�sa uppgiften s� h�r:

restv = int(input("Hur m�nga sekunder? "))

restv = sekunder
sek = restv % 60
restv //= 60
min = restv % 60
restv //= 60
tim = restv % 24
dag = restv // 24

print("Det blir",dag,"dagar,",tim,"timmar, ",min,"minuter och", sek, "sekunder")

'''
