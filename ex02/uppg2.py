
"""
Det här programmet läser in ett antal tal och beräknar dess medelvärde.
"""

antal_tal = int(input("Mata in antalet tal du vill hitta medelvärdet på: "))

inmatade_tal = []
for _ in range(antal_tal):
    inmatade_tal.append(float(input("> ")))
    
print("Du matade in", inmatade_tal)
mean = sum(inmatade_tal) / len(inmatade_tal)

print("Snittet av", inmatade_tal, "är", mean)
