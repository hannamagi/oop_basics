from praks4.inimene import Inimene

class Sodur(Inimene):
    def __init__(self, armee_nr):
        super().__init__() #inimene id tekitamine ja jk suurendamine
        self.armee_nr = armee_nr
