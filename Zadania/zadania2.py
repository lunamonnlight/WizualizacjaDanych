import numpy as np
#ZAD1
# tworzenie macierzy 1x3
matrix1 = np.array([1, 2, 3])
matrix2 = np.array([4, 5, 6])

# wyświetlenie macierzy
print("Macierz 1:")
print(matrix1)

print("Macierz 2:")
print(matrix2)

# mnożenie macierzy
result = np.dot(matrix1, matrix2)

# wyświetlenie wyniku
print("Wynik mnożenia:")
print(result)
#ZAD2
# tworzenie macierzy 3x3
matrix1 = np.array([[4, 2, 5], [1, 6, 3], [8, 7, 9]])

# wyświetlanie macierzy 3x3
print("Macierz 3x3:")
print(matrix1)

# znajdowanie najniższych wartości dla każdej kolumny i każdego rzędu w macierzy 3x3
print("Najniższe wartości dla każdej kolumny:")
print(np.min(matrix1, axis=0))
print("Najniższe wartości dla każdego rzędu:")
print(np.min(matrix1, axis=1))


# tworzenie macierzy 4x4
matrix2 = np.array([[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2], [-3, -4, -5, -6]])

# wyświetlanie macierzy 4x4
print("Macierz 4x4:")
print(matrix2)

# znajdowanie najniższych wartości dla każdej kolumny i każdego rzędu w macierzy 4x4
print("Najniższe wartości dla każdej kolumny:")
print(np.min(matrix2, axis=0))
print("Najniższe wartości dla każdego rzędu:")
print(np.min(matrix2, axis=1))
#ZAD3

# tworzenie macierzy 1x3
matrix1 = np.array([1, 2, 3])
matrix2 = np.array([4, 5, 6]).reshape((3,1))

# wyświetlanie macierzy
print("Macierz 1:")
print(matrix1)

print("Macierz 2:")
print(matrix2)

# mnożenie macierzy
result = np.dot(matrix1, matrix2)

# wyświetlanie wyniku
print("Iloczyn macierzy:")
print(result)
#ZAD4
# tworzenie macierzy 1x3 z liczbami całkowitymi
matrix1 = np.array([1, 2, 3], dtype=int)

# tworzenie macierzy 1x3 z liczbami rzeczywistymi
matrix2 = np.array([4.5, 5.5, 6.5])

# wyświetlanie macierzy
print("Macierz 1:")
print(matrix1)

print("Macierz 2:")
print(matrix2)

# mnożenie macierzy
result = np.dot(matrix1, matrix2)

# wyświetlanie wyniku
print("Iloczyn macierzy:")
print(result)
#ZAD5

# tworzenie macierzy 2x3 z różnymi wartościami
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# obliczanie sinusa dla każdej wartości macierzy
a = np.sin(matrix)

# wyświetlanie wyniku
print("Sinus dla każdej wartości macierzy:")
print(a)
#ZAD6
# tworzenie macierzy 2x3 z różnymi wartościami
matrix = np.array([[2, 4, 6], [8, 10, 12]])

# obliczanie cosinusa dla każdej wartości macierzy
b = np.cos(matrix)

# wyświetlanie wyniku
print("Cosinus dla każdej wartości macierzy:")
print(b)
#ZAD7
# macierze z wartościami sinusów i cosinusów
a = np.array([[0.84147098, 0.90929743, 0.14112001], [-0.7568025, -0.95892427, -0.2794155]])
b = np.array([[-0.41614684, -0.65364362, 0.96017029], [-0.14550003, -0.83907153, 0.84385396]])

# dodawanie macierzy
c = a + b

# wyświetlanie wyniku
print("Wynik dodawania macierzy:")
print(c)
#ZAD8
# generowanie macierzy 3x3 z losowymi wartościami
matrix = np.random.rand(3, 3)

# wyświetlanie każdego rzędu w pętli
for row in matrix:
    print(row)
#ZAD9
# generowanie macierzy 3x3 z losowymi wartościami
matrix = np.random.rand(3, 3)

# wyświetlanie każdego elementu w pętli z użyciem funkcji "flat()"
for element in matrix.flat:
    print(element)
#ZAD10
# generowanie macierzy 9x9 z losowymi wartościami
matrix = np.random.rand(9, 9)

# zmiana kształtu macierzy na 3x27
matrix_3x27 = matrix.reshape(3, 27)
print(matrix_3x27)

# zmiana kształtu macierzy na 27x3
matrix_27x3 = matrix.reshape(27, 3)
print(matrix_27x3)

# zmiana kształtu macierzy na 1x81
matrix_1x81 = matrix.reshape(1, 81)
print(matrix_1x81)
#każdy element macierzy jest jednoznacznie identyfikowany za pomocą jego pozycji, podając jego wiersz i kolumnę. Zmiana kształtu macierzy nie zmienia tej informacji, a jedynie zmienia sposób organizacji elementów w macierzy.
#ZAD11
# generowanie wektora o długości 12
vector = np.arange(12)
print(vector)

# przekształcenie wektora na macierz 3x4
matrix_3x4 = vector.reshape(3, 4)
print(matrix_3x4)

# przekształcenie wektora na macierz 4x3
matrix_4x3 = vector.reshape(4, 3)
print(matrix_4x3)

# przekształcenie wektora na macierz 2x6
matrix_2x6 = vector.reshape(2, 6)
print(matrix_2x6)

# spłaszczenie każdej z macierzy i wyświetlenie wyniku
print(matrix_3x4.flatten())
print(matrix_4x3.flatten())
print(matrix_2x6.flatten())