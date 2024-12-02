date_list = [
    '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03',
    '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09',
    '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11',
    '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09'
]

# Listák
ketezer_elott = []
szeptember = []

# Legutolsó év változó
legutolso_ev = 0

for elem in date_list:
    ev = int(elem[:4])  # Év numerikusan
    honap = elem[5:7]   # Hónap két karakter

    # Kétezer előtti dátumok
    if ev < 2000:
        ketezer_elott.append(elem)

    # Szeptemberi dátumok
    if honap == "09":
        szeptember.append(elem)

    # Legutolsó év meghatározása
    if ev > legutolso_ev:
        legutolso_ev = ev

# Kiírás
print("Ennyi elem volt kétezer előtt:", len(ketezer_elott))
print("Szeptemberre eső dátumok:", szeptember)
print("Legutolsó év:", legutolso_ev)
