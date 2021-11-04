#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:34:45 2021

@author: Army-R
"""
def refill():
    print("Get more coffee")

def drink():
    print("Ready to work")
    

def coffee():
    empty = input("Do you have coffee? ")
    if empty == "Yes" or empty == "yes":
        empty = False
    elif empty == "No" or empty == "no":
        empty = True
    else:
        print("ERROR!!")
    
    if empty == True:
        return refill()
    elif empty == False:
        return drink()
        
if __name__ == ("__main__"):
    coffee()        