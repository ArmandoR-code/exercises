#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:41:13 2022

@author: Army-R
"""
print("""
      !Encuentra la raíz cuadrada de cualquier numero!
      Elige el algoritmo a usar: 
        1- Enumeración exahusitiva
        2- Aproximación de soluciones
        3- Búsqueda binaria
        
        \x1B[3mEscribe q para salir\x1B[0m
  """)

def usr_num():
    find = int(input("Obten la raíz cuadrada de: "))
    return find

# Funcion para imprimir los resultados que no supe hacer
# def result(done, fail): 
    
def enumeracion(usr_num):
    root = 0
    
    while root**2 < usr_num:
        root += 0.1
    
    if root**2 == usr_num:
        print(f'La raiz cuadrada de {usr_num} es {root}')
    else:
        print(f'{usr_num} no tiene raiz cuadrada exacta')
       
        
        
def aproximacion(usr_num):
    epsilon = 0.01
    step = epsilon**2
    root = 0.0
    
    while abs(root**2 - usr_num) >= epsilon and root <= usr_num:
        root += step
    
    if abs(root**2 - usr_num) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {usr_num}')
    else:
        print(f'La raiz cuadrada de {usr_num} es {root}')

def binaria(usr_num):
    epsilon = 0.01
    low_lim = 0.0
    upp_lim = max(1.0, usr_num)
    root = (upp_lim + low_lim) / 2
    
    while abs(root**2 - usr_num) >= epsilon:
        if root**2 < usr_num:
            low_lim = root
        else:
            upp_lim = root
            
        root = (upp_lim + low_lim) / 2
        
    print(f"La raiz cuadrada de {usr_num} es {root}")

while True:
    option = int(input("Opción: "))
    print()
    
    if option == 1:
        print("Enumeración",)
        enumeracion(usr_num())
    elif option == 2:
        print("Aproximación")
        aproximacion(usr_num())
    elif option == 3:
        print("Búsqueda binaria")
        binaria(usr_num())
    elif option > 3 :
        print("\033[1m!Elige una de las 3 opciones ateriores!\033[0m")
    elif option == "q" or "Q": # Coregir ValueError
        break
        