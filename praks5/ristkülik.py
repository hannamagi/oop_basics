class Ristkülik:
    def __init__(self, laius, korgus, symbol):
        self.laius = int(laius)
        self.korgus = int(korgus)
        self.symbol = str(symbol)
    def __str__(self):
        ruut = []
        for i in range(self.korgus):
            ruut.append(self.symbol * self.laius)
        ruut = '\n' .join(ruut)
        return ruut
    def __add__(self, kujund2):
        return Ristkülik(self.laius + kujund2.laius, self.korgus + kujund2.korgus, self.symbol)

kujund1 = Ristkülik(10, 3, '*')
print(kujund1)
kujund2 = Ristkülik(8, 3, 'z')
print(kujund2)
print(kujund1 + kujund2)
