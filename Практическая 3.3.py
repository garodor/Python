# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 16:20:25 2025

@author: User
"""

f = float(input("Введите число f "))
k = float(input("Введите число k "))

if f < 5 and k > 2:
    R = f + k -1
elif k < 2:
    R = k**2
elif k == 2:
    R = 1
else:
    R = "формула непредусмотрина"
    
print(R)