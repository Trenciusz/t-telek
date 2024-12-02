"""Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt! A szavakat tárolja el a program egy listában!
 Az adatbekérés befejezte után írja ki a program a lista elemeit, a legrövidebb és a leghosszabb szót!"""

szavak = []

print("Adjon meg szavakat, és nyomjon ENTER-t a befejezéshez:")

while True:
    szo = input("Szó: ")
    if szo == "":  
        break
    szavak.append(szo)

print("Megadott szavak:", szavak)

if szavak:
    legrovidebb = szavak[0]
    for szo in szavak:
        if len(szo) < len(legrovidebb):
            legrovidebb = szo

    leghosszabb = szavak[0]
    for szo in szavak:
        if len(szo) > len(leghosszabb):
            leghosszabb = szo

    print("Legrövidebb szó:", legrovidebb)
    print("Leghosszabb szó:", leghosszabb)


