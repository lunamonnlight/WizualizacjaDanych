import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# zadanie 1

# x = np.arange(-3, 5, 0.3)
# rownanie = (pow(x, 2)+(3*x))/5 + np.sin(x)
# plt.plot(x, rownanie, label="wykres")
# plt.xlabel("Wykres funkcji")
# plt.ylabel("Wyniki funkcji")
# plt.legend()
# plt.show()
# print(x)
# print(rownanie)
#

# zadanie2




# x1 = np.arange(-1, 1, .25)
# x2 = np.arange(-1, 4, 0.5)
#
# y1 = np.cos(x1) * np.sin(x1)
# y2 = np.cos(x1) - np.tan(x1)
# y3 = pow(x2, 2/np.sqrt(x2))
# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.plot(x1, 2)
# plt.title('Wykres dwóch funkcji')
# plt.xlabel('x')
# plt.ylabel('Wyniki funkcji')
#
# plt.subplots_adjust(hspace=0.5)
# plt.savefig("dominika_sielawa_zad2.png")
# plt.show()


# zadanie3
# df = pd.read_csv('glass.data', header=0, sep=';', decimal='.')
# print(df)
#
# plot = sns.relplot(data=df, kind='pie',  x='mineral' , y="udzial procentowy szkla",
#                    hue='szklo', estimator= np.sum, errorbar=None,
#                    dodge=False, palette=['red', 'green', 'blue'])
# plt.savefig("dominika_sielawa_zad3.png")
# plt.show()

# zadanie4
df = pd.read_csv('glass.data', header=0, sep=',', decimal='.')
print(df)

plot = sns.barplot(data=df, x='x', y="y",
                   hue='glass', estimator= np.sum, errorbar=None,
                   dodge=False, palette=['red', 'green', 'blue'])
plot.legend(title="iLOSC KAZDEGO RODZAJU SZKLA")
plot.set(title='Wykres słupkowy')
plt.show()