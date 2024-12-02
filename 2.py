"""Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! 
A program írja ki a megadott intervallumba eső számokat és az összegüket!"""

szamok = []
osszeg = 0

while True:
    szam = int(input("Adj meg egy számot: "))
    if szam < -5 or szam > 5:
        break
    szamok.append(szam)
    osszeg = osszeg + szam

print(szamok)
print(osszeg)