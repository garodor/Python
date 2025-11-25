# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 14:30:22 2025

@author: User
"""

n = int(input("Введите размер массива: "))

x = []
a = []
b = []

for i in range(n):
    c = int(input(f"Введите {i}-ый элемент массива "))
    x.append(c)
    
for d in x:
    if d == abs(d):
        a.append(d)
    else:
        b.append(d)

print(a)
print(b)