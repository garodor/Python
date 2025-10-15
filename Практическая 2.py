# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:32:09 2025

@author: User
"""
import math

x = -4.5
y = 0.75*math.pow(10,-4)
z = -0.845 * 10**2

s = ((9 + (x - y)**2)**(1/3) / (x**2 + y**2 + 2)) -  math.exp(abs(x - y)) * math.atan(z)**3


print(s)