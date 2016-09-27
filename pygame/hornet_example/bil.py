import random

class BilFabrik():
    def __init__(self):
        self.list_of_names = ["volvo", "toyota", "tesla", "bmw", "wolksvagen", "edison"]
        self.list_of_colors = ["röd", "inte röd", "blå"]

    def get_random_bil(self):
        random_namn = random.choice(self.list_of_names)
        random_farg = random.choice(self.list_of_colors)
        
        bil = Bil(namn=random_namn, färg=random_farg)
        return bil

class Bil:
    def __init__(self, namn, färg, antal_hjul=4):
        self.namn = namn
        self.färg = färg
        self.antal_hjul = antal_hjul
        
    def fa_information_om_bilen(self):
        return "En bil som heter {}, har färgen {} och har {} hjul".format(
            self.namn, self.färg, self.antal_hjul)
        
def main():
    bilFabrik = BilFabrik()
    bilar = []
    antal_bilar = 5
    for _ in range(antal_bilar):
        ny_bil = bilFabrik.get_random_bil()
        bilar.append(ny_bil)
        
    for bil in bilar:
        print(bil.fa_information_om_bilen())
        
if __name__ == "__main__":
    main()
