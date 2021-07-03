# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:09:15 2021

@author: olive

R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not 
"""


def minmax(data):
    mininum = 0 
    maxinum = 0 
    for val in data:
        if val < mininum:
            mininum = val
        if val > maxinum:
            maxinum = val
    print((mininum, maxinum))
    
data = [150,2,3,100,5,0,-1110]
minmax(data)
    
