#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:30:45 2021

@author: Army-R
"""
print("Write a word to find if it's palindromic or not")
print()

def palindromic(word):
    word = word.replace(" ", "")
    word = word.lower()
    reverse_word = word[::-1]
    if word == reverse_word:
        return True
    else:
        return False


def main():
    word = input("Write a word: ")
    its_palindric = palindromic(word)
    if its_palindric == True:
        print("It's palindromic")
    else:
        print("It's not palindromic")

if __name__ == '__main__':
    main()
