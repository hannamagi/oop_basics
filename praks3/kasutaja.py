class Kasutaja():
    sisselogimiskatsed = 0

    def __init__(self, eesnimi, perenimi):
        self.eesnimi = eesnimi
        self.perenimi = perenimi
    def kasutajanime_maaramine(self, kasutajanimi):
        self.kasutajanimi = kasutajanimi
    def parooli_maaramine(self, parool):
        self.parool = parool
    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, kasutaja perenenimi on {1}, kasutaja kasutajanimi on  {2}. kautaja parool on {3}".format(self.eesnimi, self.perenimi, self.kasutajanimi, self.parool))
    def suurenda_sisselogimiskatsed(self):
        self.sisselogimiskatsed =+ 1
    def reset_sisselogimiskatsed(self):
        self.sisselogimiskatsed = 0

