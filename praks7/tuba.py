from praks7.aknad_ja_uksed import Aknad_ja_Uksed
class Tuba():
    def __init__(self, pikkus, laius, korgus):
        self.pindala = 2 * korgus * (pikkus + laius)
        self.aknad_uksed = []
    def lisa_Aken_Uks(self, laius, korgus):
        self.aknad_uksed.append(Aknad_ja_Uksed(laius, korgus))
    def toopindala(self):
        uus_pindala = self.pindala
        for element in self.aknad_uksed:
            uus_pindala = uus_pindala - element.pindala
        return uus_pindala