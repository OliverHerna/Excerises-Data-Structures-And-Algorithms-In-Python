# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 00:35:34 2021

@author: olive
"""

#Example of built-in functions
print(chr(250))

#Separator
print('a','b','c',sep=':' )

#Final Element
print('a', 'b','c', end=':' )

#Casted input  to int
year = int(input(' In what year were you born? '))
print(year, end='!')

reply = input( 'Enter x and y, separated by spaces:' )
pieces = reply.split( ) # returns a list of strings, as separated by spaces
x = float(pieces[0])
y = float(pieces[1])