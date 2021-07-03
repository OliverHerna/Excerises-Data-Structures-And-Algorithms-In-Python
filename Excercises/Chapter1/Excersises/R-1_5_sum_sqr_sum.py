# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:41:44 2021

R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function

@author: olive
"""

def sum_other(n):
    nums = []
    while (n > 0):
        nums.append(pow(n,2))
        n -= 1
    return sum(nums)

    
print('Addition with sum: ',sum_other(5))