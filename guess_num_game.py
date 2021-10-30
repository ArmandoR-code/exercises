#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:45:09 2021

@author: Army-R
"""
import random

print("Play the Game!! Reed my mind\nGuess a number between 1 and 100")
print()

def main():
    random_num = random.randint(1, 100 + 1)
    user_num = int(input("Gess the number: "))
    print()

    while user_num != random_num:
        if user_num < random_num:
            print("Look for a biger number ")
            print()
        else:
            print("Look for a small number ")
            print()
        print()
        user_num = int(input("Choose another number "))
        print()
    print()
    print("You winn!!")

if __name__ == "__main__":
    main()
