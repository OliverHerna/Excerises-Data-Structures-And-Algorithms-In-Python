# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:24:07 2021

@author: olive

R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

"""
def sum_sqr(n):
    sumn = 0 
    if n == 0 :
        return sumn
    sumn += pow(n,2) + sum_sqr(n-1)

print(sum_sqr(3))
"""

def sum_sqr(n):
    sumn = 0
    while(n > 0):
        sumn += pow(n, 2)
        n -= 1
    return sumn

print('Addition without sum: ',sum_sqr(3))

        


