#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 20:34:08 2021

@author: Army-R
"""
# Write a paragraph and find out what the longest word is 

txt = input("Write a paragraph: ")
print()

# An empty string
longest = ""

# Compare de len of each word of the list
# with the len of the same list words 
for word in txt.split():
    if len(word) > len(longest):
        longest = word

# Print the longest word
print(longest)

    