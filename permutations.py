#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:30:02 2022

@author: Army-R
"""
# Permutations 
# Formula nPr n!/(n-r)!
print(""" 
      Permutations 
      
      Obtain the number of permutation calculated with the following formula
      
      nPr = n!/(n-r)!
      """)

n = int(input("n = "))
r = int(input("r = "))

def subtract(n, r):
    return (n - r)

def factorial_n(n):
    if n == 1:
        return 1
    else:
        return (n * factorial_n(n-1))

def factorial_r(subtract):
    if subtract == 1 or subtract == 0:
        return 1
    else:
        return (subtract * factorial_r(subtract-1))
     

def permutation(factorial_n, factorial_r):
    return (factorial_n / factorial_r)

print()
print(f"The number of permutations of {n} in {r} are: ", permutation(factorial_n(n), factorial_r(subtract(n, r))))
