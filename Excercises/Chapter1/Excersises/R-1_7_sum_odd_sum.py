# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:49:40 2021

R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying 
on Python’s comprehension syntax and the built-in sum function.

@author: olive
"""

def odd_sum(n):
    num_collection = []
    while n > 0:
        if(pow(-1, n) < 0):
            num_collection.append(pow(n, 2))
        n -= 1
    return sum(num_collection)

print(odd_sum(5))
    
    
