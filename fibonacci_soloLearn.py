#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:40:04 2022

@author: Army-R
"""

def fibonacci(n):
    if n <= 1:
        return 1
    else:
        a = 0
        b = 1
        while a < n:
            print(fibonacci(n-a) + fibonacci(n-b))
            a = b
            b += 1
    
            
            
   
print(fibonacci(6))            