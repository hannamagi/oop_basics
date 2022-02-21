from praks2.restoraan import Restoraan
class Jäätisekiosk(Restoraan):
    kioski_nimi = ""
    pakub = ""
    jaatise_valik = ""
    def naita_jaatise_valik(self):
        print(self.jaatise_valik)
kiosk = Jäätisekiosk()
kiosk.kioski_nimi = "Hanna kiosk"
kiosk.pakub = "Jäätised"
kiosk.jaatise_valik = ("vanilli, šokolaad, maasika")
kiosk.kirjelda_restoran()
kiosk.naita_jaatise_valik()
