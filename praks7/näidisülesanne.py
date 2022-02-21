class Aknad_ja_Uksed():
    def __init__(self, laius, korgus):
        self.pindala = laius * korgus
class Tuba():
    def __init__(self, p, l, k):
        self.pikkus = p
        self.laius = l
        self.korgus = k
        self.aknad_uksed = []
    def lisa_Aken_Uks(self, laius, korgus):
        self.aknad_uksed.append(Aknad_ja_Uksed(laius, korgus))
    def täisPind(self):
        return 2 + self.korgus * (self.pikkus + self.laius)
    def toopindala(self):
        uus_pindala = self.täisPind()
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala
    def tapeedid(self, tp, tl):
        return int(self.toopindala() / (tp * tl)) + 1

p = float(input("Pikkus:"))
l = float(input("Laius: "))
k = float(input("Kõrgus: "))
tuba = Tuba(p, l, k)
vastus = input("Kas olemas aknad/uksed? jah/ei")
while vastus == "jah":
    l = float(input("Akna/Ukse laius "))
    k = float(input("Akna/Ukse kõrgus "))
    aken_uks = Aknad_ja_Uksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas olemas aknad/uksed? jah/ei")

print("Tapeedi rulli mõõdud: ")
tl = float(input("Tapeedi laius "))
tp = float(input("Tapeedi pikkus "))

print("Tapeedid on vaja pleepida " + str(tuba.toopindala()) + "ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl))