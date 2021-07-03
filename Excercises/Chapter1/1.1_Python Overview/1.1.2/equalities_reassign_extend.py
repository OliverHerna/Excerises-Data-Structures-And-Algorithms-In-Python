# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:42:10 2021

@author: olive
"""

alpha = [1,2,3]
#alias for alpha
beta = alpha
#extends the original list with two more elements 
beta += [4,5]
#reassigns beta to a new list
beta = beta + [6,7]
print(beta)
print(alpha)