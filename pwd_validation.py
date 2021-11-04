#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:19:27 2021

@author: Army-R
"""
# Password validator
import getpass
from string import punctuation

print(
"""
Validation rules:
    No spaces
    Lenght between 8 and 16 characters
    At least 1 special character
    Al least 1 number
    At least 1 uppercase
"""
)
print()

def main(pwd):
    # No spaces
    if " " in pwd:
        return "The password must not have spaces"
    # Lenght b/w 8 and 16 characters
    if len(pwd) not in range(8, 17):
        return "The password must be between 8 and 16 characters"
    # 1 special character
    special_char = [True for x in pwd if x in punctuation]
    if len(special_char) == 0:
        return "The password must have at least 1 special character"
    # 1 number
    num = any(x.isdigit() for x in pwd)
    if not num:
        return "The password must have at least 1 number"
    # 1 uppercase
    capital = any(x.isupper() for x in pwd)
    if not capital:
        return "The password must have 1 uppercase"
    
    return f"Your password: {pwd} passed the validation test"

pwd = getpass.getpass("Enter your password: ")

print(main(pwd))

if __name__ == "__main__":
    main(pwd)

# Make unit testing