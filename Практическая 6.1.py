# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 13:47:32 2025

@author: User
"""

n = int(input("Введите размер массива: "))

x = []
min_value = x
min_index = 0
for i in range(n):
    a = int(input(f"Введите {i}-ый элемент массива "))
    x.append(a)

min_value = a
min_index = 0

for i in range(1, n):
    if x[i] < min_value:
        min_value = x[i]
        min_index = i

print(f"Минимальный элемент: {min_value}")  
print(f"Индекс минимального элемента: {min_index}")