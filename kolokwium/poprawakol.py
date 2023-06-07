import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Zadanie1
# x = np.arange(2, 9, 0.5)
# y = (np.sqrt(x)+3*x)/((4*x)+5)
#
#
# plt.plot(x, y, label='f(x)')
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
#
# plt.axis([2, 9, 0.5, 1])
#
# plt.legend()
#
# plt.title('Wykres funkcji f(x)  dla x[2,9]')
# plt.savefig("Dominika_Sielawa_Zad1.png")
# plt.show()

# zadanie2

# x = np.arange(-3, 5, 0.5)
# y = pow(x, 2) + (np.sin(pow(x,2))/ x)
#
# plt.plot(x, y, "r^", label="f(x)")
#
# plt.xlabel('x')
# plt.ylabel('Wyniki Funkcji')
#
# plt.axis([-3, 5, -1, 25])
#
# plt.legend()
#
# plt.title('Wykres funkcji f(x)  dla x[-3, 5]')
# plt.savefig("Dominika_Sielawa_zad2.png")
# plt.show()
# Zadanie3
# #
# df = pd.read_csv('handel.csv', header=0, sep=',', decimal='.')
# wartosc = df.groupby('Wyszczegolnienie')['Wartosc'].sum()
#
# plt.pie(wartosc.index, wartosc.values)
#
# for i, value in enumerate(wartosc.values):
#     plt.text(i, value, str(value), ha='center', va='bottom')
#
# plt.title('Wartosc wyszczegolnionych')
# plt.xlabel('Wyszczegolnione')
# plt.ylabel('Wartosc')
# plt.legend()
# # plt.savefig("Dominika_Sielawa_zad3.png")
# # plt.show()
#
# # Zadanie4
#
# df = pd.read_csv('handel.csv', header=0, sep=',', decimal='.')
# wartosc = df.groupby('Wyszczegolnienie')['Wartosc'].sum()
# ax = plt.subplots()
# plt.pie(wartosc.index)
#
# for i, value in enumerate(wartosc.values):
#     plt.text(i, value, str(value), ha='center', va='bottom')
#
# plt.title('Wartosc wyszczegolnionych')
# plt.xlabel('Wyszczegolnione')
# plt.ylabel('Wartosc')
# plt.legend()
# plt.savefig("Dominika_Sielawa_zad4.png")
# plt.show()