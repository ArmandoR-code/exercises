#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:08:53 2021

@author: Army-R
"""
# Hashes with passlib module
from getpass import getpass as gp
from passlib.hash import pbkdf2_sha256 as sha256
from passlib.hash import bcrypt as bc
from passlib.context import CryptContext as cc

# Create a hash for the password
pwd_hash = sha256.hash('Admin1234.')
print(pwd_hash)
print()

# Verify the hash
correct = sha256.verify('Admin1234.', pwd_hash)
print(correct, ':The hash match with the passsword')
print()

incorrect = sha256.verify('Password1234.', pwd_hash)
print(incorrect, ':The hash did not match with the password')
print()

# Define the round of the hash
print(sha256.default_rounds)
print()

new_round = sha256.using(rounds=1111)
new_hash = new_round.hash('Password1234.')
print(new_hash)
print()

# Using bcrypt as bc from the passlib.hash module
print(bc.setting_kwds)
print()
print(bc.default_rounds)

# Change default round value. Make it slower
hasher = bc.using(rounds=13)

pwd = gp(prompt='Enter your password: ')  
print()

hashed_pwd = hasher.hash(pwd)

print(hashed_pwd)
print()

# Verify the password
print(hasher.verify(pwd, hashed_pwd))

# Using CryptoContext as cc form the passlib.context
ctx = cc(schemes=['bcrypt', 'argon2', 'scrypt'], 
         bcrypt_rounds=14) 

pwd = gp(prompt='Enter your password: ')
hashed_pwd = ctx.hash(pwd)
print(hashed_pwd)

# verify the password
print(ctx.verify(pwd, hashed_pwd))

