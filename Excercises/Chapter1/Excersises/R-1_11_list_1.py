# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:18:43 2021

R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

@author: olive
"""

nums = []
n = 1

while (n < 257):
    nums.append(n)
    n *= 2 
    
print(nums)

