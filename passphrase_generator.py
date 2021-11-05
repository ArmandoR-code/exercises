#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:31:31 2021

@author: Army-R
"""
# Passphrase generator
# https://xkcd.com/936/

from xkcdpass import xkcd_password as xp

words = xp.generate_wordlist(min_length=5, max_length=8)

passphrase = xp.generate_xkcdpassword(words, numwords=4)

print('New passphrase: ', passphrase)
