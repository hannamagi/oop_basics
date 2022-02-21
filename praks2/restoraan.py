class Restoraan():
    restoraani_nimi = ""
    soogi_tyyp = ""
    def kirjelda_restoran(self):
        print(self.restoraani_nimi + ". " + self.soogi_tyyp)
    def ava_restoraan(self):
        print("Restoraan on avatud")
restoraan1 = Restoraan()
restoraan1.restoraani_nimi ="Kajake"
restoraan1.soogi_tyyp = "meretoit"
restoraan1.kirjelda_restoran()
restoraan1.ava_restoraan()

restoraan2 = Restoraan()
restoraan2.restoraani_nimi = "Hani"
restoraan2.soogi_tyyp = "halelihast tehtud praed"
restoraan2.kirjelda_restoran()
restoraan2. ava_restoraan()

restoraan3 = Restoraan()
restoraan3.restoraani_nimi = "Moona"
restoraan3.soogi_tyyp = "Värskeid praade, suppe, magustoite Moona köögist"
restoraan3.kirjelda_restoran()
restoraan3. ava_restoraan()