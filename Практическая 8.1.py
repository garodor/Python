# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 00:18:13 2025

@author: User
"""

def is_magic_square(matrix):
    n = len(matrix)
    # сумма по первой строке
    target_sum = sum(matrix[0])

    # проверка суммы по каждой строке
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # проверка суммы по каждому столбцу
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False

    return True

# ввод размера матрицы
n = int(input("Введите размер матрицы n: "))

# ввод элементов матрицы
matrix = []
print("Введите элементы матрицы построчно:")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# проверка и вывод результата
if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")
