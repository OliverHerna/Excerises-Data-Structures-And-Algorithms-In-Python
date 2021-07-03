# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:46:55 2021

C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.

@author: olive
"""

"""
aux_num
For index from data lenght to data lengt divided by 2 
    aux_num is equal to index from data
    index from data is equal to value in lenght from data - index
    value in lenght from data - index is equal to aux
"""

data = [2,6,5,9,11,3,9,4,100]

print(len(data))

aux = 0
for val in range(0, len(data)//2):
    aux = data[val] 
    data[val] = data[len(data)-(1+val)]
    data[len(data)-(val+1)] = aux
    
print(data)
    