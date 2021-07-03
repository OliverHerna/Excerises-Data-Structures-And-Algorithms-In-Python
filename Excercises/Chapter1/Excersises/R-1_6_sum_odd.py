# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:43:05 2021

R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

@author: olive
"""

def odd_sum(n):
    sumn = 0 
    while n > 0:
        if(pow(-1,n) < 0):
           sumn += pow(n, 2)
        n -=1
    return sumn

print(odd_sum(5))           
               

        