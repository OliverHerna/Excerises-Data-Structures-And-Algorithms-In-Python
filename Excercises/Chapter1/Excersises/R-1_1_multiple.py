# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:39:21 2021

@author: olive
"""

"""
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

"""


def isMultiple(n, m):
    if(m%n != 0):
       return False
    else:
       return True
    
n = int(input('Enter a number:'))
m = int(input('Enter another number:'))

print('\n', isMultiple(n,m))