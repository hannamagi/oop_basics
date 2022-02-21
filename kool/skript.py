from opimine import *
teemad = Andmed("klass", "objekt", "pärilus", "polümorfism", "kapseldus")
anna = Õpetaja()
kadi = Õpilane()
mati = Õpilane()

mati.õpib(teemad[3])
mati.õpib(teemad[2])
mati.õpib(teemad[1])

mati.unustada()