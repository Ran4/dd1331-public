print("Det här programmet kommer att beräkna antalet termer N som behövs för att summan av 1/i för i = 1..N ska nå upp till ett visst mål")

target_sum = int(input("Vad är ditt slutmål?"))

term_sum = 0.0
i = 1
while term_sum < target_sum:
    term = 1 / i
    term_sum += term
    i += 1
    
number_of_terms = i - 1
print("antal termer för att nå upp till", target_sum,
        "är lika med", number_of_terms)
