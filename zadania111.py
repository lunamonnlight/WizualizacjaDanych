import pandas as pd
import numpy as np

# # Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
# print(s)
#
# #DataFrame
# #tworzenie dataframe na podstawie słownika
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#   'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#   'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# # #DataFrame przechowuje typ dla każdej kolumny co możemy sprwadzić wpisując
# print(df.dtypes)
# # #możemy również w prosty sposób stworzyć serię danych -czyli
# # próbki dla kolejnych #dat, pomiarów czasu
# daty = pd.date_range('20210324', periods=5)
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)
# # #biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
# #CSV, odczyt i zapis


xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
