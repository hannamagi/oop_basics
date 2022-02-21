from praks4.admin import Admin

kasutaja1 = Admin("Mari", "Maarikas")
kasutaja1.kasutajanime_maaramine("MariM")
kasutaja1.parool = "maasikas"
kasutaja1.kirjelda_kasutaja()
kasutaja1.suurenda_sisselogimiskatsed()
valik = input("Kas soovite lisada õiguseid? (jah/ei): ")
while valik == "jah":
    valik2 = int(input("Milliseid järgnevatest varjantides soovite teha? 1. Lubatud lisada kasutaja, 2. Lubatud eemaldada kasutajad, 3. lubatud blokeerida kasutaja, 4. midagi muud: "))
    if valik2 == 1:
        kasutaja1.privileegid.append("Lubatud lisada kasutajad")
    if valik2 == 2:
        kasutaja1.privileegid.append("Lubatud eemaldada kasutajad")
    if valik2 == 3:
        kasutaja1.privileegid.append("Lubatud blokeerida kasutajad")
    if valik2 == 4:
        kasutaja1.privileegid.append(input("Millideid õiguseid soovite lisada? "))
    valik = input("Kas soovite veel õigusi lisada? (jah/ei): ")
print("Kasutaja privileegid on järgmised:")
kasutaja1.naita_privileegid()