import random
#zadanie 1
A = []
for x in range(1, 10):
    A.append(1-x)
print(A)

B = []
for x in range(0, 7):
    B.append(pow(4, x))
print(B)

C = []
for x in range(len(B)):
    if B[x] % 2 == 0:
        C.append(B[x])

print(C)

# zadanie 2

lista1 = []
for x in range(1, 10):
    num = random.randint(1, 100)
    if num % 2 == 0:
        lista1.append(num)

print(lista1)

# zadanie3

zakupy = {
    'czekolada': 'sztuka',
    'pomarancze': 'kilogram',
    'sok': 'sztuka',
    'pierogi': 'opakowanie',
    'cytryna': 'sztuka'
}
sztuki = []
for nazwa, jednostka in zakupy.items():
    if jednostka == 'sztuka':
        sztuki.append(nazwa)

print(sztuki)

# zadanie4

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

if( pow(a,2)+ pow(b,2) == pow(c,2)):
    print("Trojkat jest prostokatny")
elif(pow(b,2) + pow(c,2) == pow(a,2)):
    print("Trojkat jest prostokatny")
elif(pow(a,2) + pow(c,2) == pow(b,2)):
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")

# zadanie5
def funkcja(podstawa1=6, podstawa2=3,wysokosc=5):
    print("Pole trapezy wynosi:", ((podstawa1+podstawa2)*wysokosc)/2)

funkcja(1,3,5)
funkcja()

# zadanie6

def zadanie6(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(1, ile):
        iloczyn *= a + (i*b)
        return iloczyn

print(zadanie6(1,5,3))

# zadanie8



