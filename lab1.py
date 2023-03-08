# a = 'a'
# b = 4
# c = 3.5
# d = (b, c)
# print(d)
# e = b + c
# print(e)
# f = b // c
# print(f)
# g = b % c
# print(g)
# i = c**2
# print(i)
# j = pow(5, 2)
# print(j)
# # k = 5**1/2
# # m = pow(5, 1/2)
# print('b = b + 2')
# b += 2
# print(b)
#
lista = ['a0', 2, 4, 5, [7, 8, 11], 5.5]
#
# print(lista[4])
# lista.append(6.5)
# print(lista)
# #dodanie elementu na liscie
# lista.append(7)
#
# #dodawanie kilku elementow na koncu listy
# lista.extend([8, 2, 7, 39.2])
#
# #usuwanie elementu po indexie
# lista.pop(4)
#
# #usuwanie elementu po wartosci elementu
# lista.remove('a0')
#
# #odwrocenie listy
# lista.reverse()
#
# #sortowanie
# lista.sort()
# print(lista)
# #
# slownik = {'a': 1, 3: 1, 5: 'b'}
# print(slownik)
#
# print(slownik['a'])
#
# slownik['klucz'] = 'wartosc'
# print(slownik)
#
# slownik.pop('a')
# print(slownik)
#
#
# print('a = %(zm)d' %{'zm' : 12})
# print('a = {} , b = {}'.format(12, 14))

# if warunek:
#     instrukcja 1
#     insrukcja 2
# elif warunek 2:
#     instrukcja 1
#     instrukcja 2
# else:
# instrukcja

# a = input('podaj a: ')
# b = input('podaj b: ')
# c = input('podaj c: ')
# d = input('podaj d: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)

# if a == b:
#     print("A jest rowne B")
# elif a > b:
#     print("a jest wieksze od b")
# else:
#     print("b jest wieksze od a")
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print("A nie jest wieksze od B lub C nie jest wieksze od D")
# #
# for element in sekwencja:
#     instrukcja 1
#     instrukcja 2
# else:
#     instrukcja 1
#     instrukcja 2

# for x in range(1, 6, 1):
#     print(x)
#
# for x in lista:
#     print(x)
#
# for x in range(0, len(lista), 1):
#     print(lista[x])
#
# while warunek:
#     instrukcje
# #
# else:
#     instrukcja
#
# licznik = 0
# while licznik != len(lista):
#     print(lista[licznik])
#     licznik += 1
#
# liczby = [ 3, 5, 37, 28, 37.2, 394, 2938, 2, 38, 3.2]
# licznik = 0
# a = int(input('Podaj a: '))
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#     licznik +=1


liczby = [1, 2, 2, 2, 2, 2, 3]
licznik = 0
while licznik != len(liczby):
    if liczby[licznik] == 2:
        liczby.remove(liczby[licznik])
    else:
        licznik += 1

print(liczby)
