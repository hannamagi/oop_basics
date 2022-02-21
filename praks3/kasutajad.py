from praks3.kasutaja import Kasutaja
kasutaja1 = Kasutaja("Mari", "Maarikas")
kasutaja1.kasutajanime_maaramine("MariM")
kasutaja1.parool = "maasikas"
kasutaja1.kirjelda_kasutaja()
kasutaja1.suurenda_sisselogimiskatsed()
print("Kasutaja on sisseliginud " + str(kasutaja1.sisselogimiskatsed) + " korda")
kasutaja1.reset_sisselogimiskatsed()

kasutaja2 = Kasutaja("Vello", "Vaarikas")
kasutaja2.kasutajanime_maaramine("VelloV")
kasutaja2.parool = "vaarikas"
kasutaja2.kirjelda_kasutaja()
kasutaja2.suurenda_sisselogimiskatsed()
print("Kasutaja on sisseliginud " + str(kasutaja2.sisselogimiskatsed) + " korda")
kasutaja2.reset_sisselogimiskatsed()

kasutaja3 = Kasutaja("Tiina", "Tikker")
kasutaja3.kasutajanime_maaramine("TiinaT")
kasutaja3.parool = "tikker"
kasutaja3.kirjelda_kasutaja()
kasutaja3.suurenda_sisselogimiskatsed()
print("Kasutaja on sisseliginud " + str(kasutaja3.sisselogimiskatsed) + " korda")
kasutaja3.reset_sisselogimiskatsed()
