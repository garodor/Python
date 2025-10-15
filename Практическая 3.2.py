# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 16:12:13 2025

@author: User
"""

a = input('Введите двухзначное число ')



if len(a) == 2 and a.isdigit():

    if a[0] == a[1]:
        print('Да')
    else:
        print('Нет')
        