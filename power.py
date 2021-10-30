#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:03:23 2021

@author: Army-R
"""
print("This program output the power of 2 to the limit you choose")
print()

def main():
    limit =  int(input("Power limit: "))
    NUMBER = 2  # Capitalize for constants

    counter = 0
    result = NUMBER ** counter

    while result < limit:
        print(f"2 power {counter} equals {result} ")
        counter += 1
        result = NUMBER ** counter

if __name__ == "__main__":
    main()
