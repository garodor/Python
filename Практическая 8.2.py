# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 13:18:02 2025

@author: User
"""

N = int(input("Введите размер матрицы N: "))
A = []

# заполнение матрицы
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# перестановка первого и последнего столбцов
for i in range(N):
    A[i][0], A[i][N-1] = A[i][N-1], A[i][0]

# вывод матрицы
for row in A:
    print(' '.join(map(str, row)))