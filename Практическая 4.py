# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 16:47:22 2025

@author: User
"""
a = int(input('Введите число a '))
b = int(input('Введите число b '))
i = 0
if a < b:
    
    for i in range(b):
        print(a + i)
    i += 1
else:
    for i in range(a):
        print(a - i)
    i += 1