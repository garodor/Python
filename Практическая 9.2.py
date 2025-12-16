# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:28:55 2025

@author: User
"""

def abc():
    num = int(input())
    if num==0:
        return -1,-1
    first_max, second_max = abc()
    if first_max == -1:  
        return num, -1
    elif num > first_max: 
        return num, first_max
    elif num > second_max or second_max == -1:
        return first_max, num
    else:
        return first_max, second_max

print("Введите последовательность: ")
first, second = abc()

if second == -1:
    print("В последовательности меньше двух элементов")
else:
    print("Второй по величине элемент: ", second)