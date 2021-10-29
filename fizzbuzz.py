#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:55:23 2021

@author: Army-R
"""

# FizzBuzz exercise
# It takes an input n and outputs the numbers from 1 to n.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, prints "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, output "FizzBuzz".

n = int(input("Type a number: "))

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        