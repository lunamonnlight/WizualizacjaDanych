# # zadanie1
# plik1 = open("plik1.txt", "r+")
# A = []
# for x in range(0, 31):
#     A.append(x*2)
# print(A)
# plik1.writelines(str(A))
# plik1.close()
# # zadanie2
#
# with open("plik1.txt", "r") as plik:
#     for linia in plik:
#         print(linia, end="")
#
# # zadanie3
#
# with open("tekst.txt", "r") as plik:
#     for linia in plik:
#         print(linia, end="")
# zadanie4

#
# class NaZakupy:
#     """Lista zakupowa"""
#     nazwa_produktu = ''
#     ilosc = ''
#     jednostka_miary = ''
#     cena_jed = ''
#     def konstruktor(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         return (nazwa_produktu,' ', ilosc, ' ', jednostka_miary, ' ', cena_jed)
#     def ile_produktu(self, nazwa_produktu, ilosc, jednostka_miary):
#         return(nazwa_produktu, " ", ilosc, " ", jednostka_miary)
#     def ile_kosztuje(self, nazwa_produktu, ilosc, cena_jed):
#         return(nazwa_produktu, ' - ', ilosc*cena_jed)
#
# print(obiekt1)
#
# obiekt1 = NaZakupy()
# ##                                       ZAD_5
# class CiagArytmetyczny:
#     def __init__(self):
#         self.elementy = []
#
#     def wyświetl_dane(self):
#         print("Elementy ciągu arytmetycznego:", self.elementy)
#
#     def pobierz_elementy(self):
#         n = int(input("Podaj ilość elementów ciągu: "))
#         for i in range(n):
#             x = int(input("Podaj wartość elementu: "))
#             self.elementy.append(x)
#
#     def pobierz_parametry(self):
#         a = int(input("Podaj pierwszą wartość ciągu: "))
#         r = int(input("Podaj różnicę ciągu: "))
#         n = int(input("Podaj ilość elementów ciągu: "))
#         self.elementy = [a + i * r for i in range(n)]
#
#     def policz_sume(self):
#         suma = sum(self.elementy)
#         print("Suma elementów ciągu arytmetycznego wynosi:", suma)
#
#     def policz_elementy(self):
#         if len(self.elementy) > 0:
#             n = len(self.elementy)
#             a = self.elementy[0]
#             r = self.elementy[1] - self.elementy[0]
#             an = a + (n - 1) * r
#             print("Liczba elementów ciągu arytmetycznego wynosi:", n)
#             print("Ostatni element ciągu wynosi:", an)
#         else:
#             print("Nie wygenerowano jeszcze elementów ciągu.")
#
# ciag = CiagArytmetyczny()
#
# ciag.pobierz_elementy()
#
# ciag.wyświetl_dane()
#
# ciag.pobierz_parametry()
#
# ciag.wyświetl_dane()
#
# ciag.policz_sume()
#
# ciag.policz_elementy()
#
# #                                       ZAD_6
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += ile_krokow * self.krok
#
#     def idz_w_dol(self, ile_krokow):
#         self.y -= ile_krokow * self.krok
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= ile_krokow * self.krok
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x += ile_krokow * self.krok
#
#     def pokaz_gdzie_jestes(self):
#         print(f"Aktualne współrzędne: x={self.x}, y={self.y}")
#
# robaczek = Robaczek(0, 0, 1)
# robaczek.pokaz_gdzie_jestes()
# robaczek.idz_w_gore(5)
# robaczek.pokaz_gdzie_jestes()
# robaczek.idz_w_prawo(6)
# robaczek.pokaz_gdzie_jestes()
# robaczek.idz_w_dol(2)
# robaczek.pokaz_gdzie_jestes()
# robaczek.idz_w_lewo(3)
# robaczek.pokaz_gdzie_jestes()

