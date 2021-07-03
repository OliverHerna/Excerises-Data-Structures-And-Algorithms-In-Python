# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:25:34 2021

R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a more 
basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.

@author: olive
"""
from random import choice
from random import randrange

print(choice(range(2, 100, 2)))


#using only randrange
print(randrange(2,100,2))