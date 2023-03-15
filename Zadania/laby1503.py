# zadanie 1
import math
a = math.exp(10)
print("Wartosc e^10 wynosi: ", a)

print(math.pow(math.log(math.e, 5 + math.pow(math.sin(8), 2)), 1/6))

print(math.floor(3.55))

print(math.ceil(4.80))

#Zadanie 2

imie = "DOMINIKA"
nazwisko = "SIELAWA"

print(str.capitalize(imie), str.capitalize(nazwisko))

#zadanie 3

str = "Que tú me tienes a quinientos y perdío Mentiras son dividí contigo Pero esa vuelta no es pa mí Que tú me quieres amarrao aquí Oye mami, vuélvete loca Arúñame la espalda y muérdeme la boca Oye papi, vuélveme loca Arúñame la espalda y muérdeme la boca";

sub = "boca";
print(str.count(sub, 4, len(str)))

#zadanie 4

zmienna = "bardzo.dlugi.wyraz"

print(zmienna[1], zmienna[len(zmienna)-1])

#zadanie5

print(zmienna.split(sep="."))

#zadanie6

a = 0xff12
print(a)
print('{0}'.format(a))

b = 8.273837

print(b)
print(format(b))

c = "girl"
print(c)
print(format(c))

#zadanie 7

sporty = ['tenis zmienny', 'siatkowka', 'koszykowka']
sporty.reverse()
print(sporty)
sporty.extend(['unihokej', 'piłka nożna'])
print(sporty)
#zadanie 8

skroty = {
    "np.": "na przykład",
    "itd.": "i tym podobne",
    "tj.": "to jest",
    "ocb": "o co biega",
    "ct": "co tam",
    "cr": "co robisz",
    "kc": "kodeks cywilny"
}
for skrot, rozw in skroty.items():
    print("{} - {}".format(skrot, rozw))
#zadanie 9
gry = {
    "GTA": "Grand Theft Auto",
    "CS": "Counter strike",
    "LOL": "League of legends"
}
print(len(gry))

#zadanie 10
a = input("Napisz tekst: ")
l_a = a.count("a")
print("Liczba wystąpień słowa 'a':", l_a)

# zadanie 11

zad11a = int(input("Podaj pierwszą liczbę całkowitą: "))
zad11b = int(input("Podaj drugą liczbę całkowitą: "))
zad11c = int(input("Podaj trzecią liczbę całkowitą: "))

if zad11a > zad11b and zad11a > zad11c:
    print("Największa liczba to", zad11a)
elif zad11b > zad11a and zad11b > zad11c:
    print("Największa liczba to", zad11b)
else:
    print("Największa liczba to", zad11c)

# zadanie 12

lista = {1, 873, 092.2, 873, 83.2673, 273.2, 27638.2}

for i in lista:
    print(pow(i, 2))

#zadanie 13

l_parzyste = []
licznik = 0
while licznik < 10:
    liczba = int(input("Podaj liczbę do zadania 13: "))
    if liczba % 2 == 0:
        l_parzyste.append(liczba)
    licznik += 1
print("Liczby parzyste:", l_parzyste)