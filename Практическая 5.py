# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 12:44:19 2025

@author: User
"""

text = input("Введите строку: ")

total_chars = len(text)

count_replacements = text.count('а')  
new_text = text.replace('а', 'о')  

print(f"Исходная строка: {text}")  
print(f"Измененная строка: {new_text}")  
print(f"Количество замен: {count_replacements}")  
print(f"Общее количество символов: {total_chars}")  