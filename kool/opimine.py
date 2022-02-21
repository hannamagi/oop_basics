#mooduli importimine
from random import randint
#kasside loomine
class Andmed:
    """Andmete hoidmise klass"""
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]

class Õpetaja:
    """Õpetaja klass õpetab õpilastele andmeid"""
    def õpetab(self, info, *õpilane):
        """Õpetab teadmisi õpilastele, vajab õpetava infot ja õpilaste nimesid"""
        for i in õpilane:
            i.õpib(info)

class Õpilane:
    """klass, mis hoiab õpitud teadmisi"""
    def __init__(self):
        self.teadmised = []
    def õpib(self, info):
        """Õpetab teadmisi õpilastele, vajab õpetava infot, prindib õpitud teema"""
        self.teadmised.append(info)
        print("Õpilane õppis teemad: " + info)
    def unustada(self):
        """Kusututab teadmised õpilase objektist"""
        voimalus = randint(1, 10)
        if voimalus <= 5:
            """kustutab teadmised ja prindib unsutatud teema"""
            voimalus2 = randint(0, len(self.teadmised) - 1)
            print("Õpilane unustas järgmised teemad: " + self.teadmised[voimalus2])
            self.teadmised.pop(voimalus2)
        else:
            pass