class Kasutaja():
    eesnimi = ""
    perenimi =""
    vanus = 0

    def kirjelda_kasutaja(self):
        print("Kasutaja eesnimi on {0}, kasutaja perenenimi on {1}, kasutaja vanus on {2}".format(self.eesnimi, self.perenimi, self.vanus))

    def tervita_kasutaja(self):
        print("Tere! {0} ".format(self.eesnimi ))

kasutaja1 = Kasutaja()
kasutaja1.eesnimi = "Mari"
kasutaja1.perenimi = "Maarikas"
kasutaja1.vanus = 25
kasutaja1.kirjelda_kasutaja()
kasutaja1.tervita_kasutaja()

kasutaja2 = Kasutaja()
kasutaja2.eesnimi = "Vello"
kasutaja2.perenimi = "Vaarikas"
kasutaja2.vanus = 19
kasutaja2.kirjelda_kasutaja()
kasutaja2.tervita_kasutaja()

kasutaja3 = Kasutaja()
kasutaja3.eesnimi = "Tiina"
kasutaja3.perenimi = "Tikker"
kasutaja3.vanus = 30
kasutaja3.kirjelda_kasutaja()
kasutaja3.tervita_kasutaja()