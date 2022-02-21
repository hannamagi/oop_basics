class Ristkülik():
    def __init__(self, l, k):
        self.__laius = Ristkülik.__väärtusekontroll(l)
        self.__kõrgus = Ristkülik.__väärtusekontroll(k)
    def määra_laius(self, l):
        self.__laius = Ristkülik.__väärtusekontroll(l);
    def määra_kõrgus(self, k):
        self.__kõrgus = Ristkülik.__väärtusekontroll(k);
    def __väärtusekontroll(väärtus):
        if väärtus < 0:
            return abs(väärtus)
        else:
            return väärtus
    def __str__(self):
        return "Ristkülik: " + str(self.__laius) + " X " + str(self.__kõrgus)
kujund_1 = Ristkülik(3, 4)
print(kujund_1)
kujund_2 = Ristkülik(-8, -5)
print(kujund_2)
