# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 02:01:18 2018

@author: Colton
"""

cube = 777
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
    
print('num_guesses =', num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, 'is close to the cube root of', cube)


