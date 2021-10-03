#!/usr/bin/env python3
"""
    Propósito: calcular la constante de Madelung de cristales de NaCl
    Ejercicio 2.9 del libro de Mark newman, Computational Physics
    Autor: Adrián Hernández
    Fecha: 3 de octubre de 2021
"""
from numpy import sqrt
from time import time
inicio = time()

#   declarar la variable para la cte de Madelung

M = 0.0  

#   declarar el tamaño de la red L

L = int(input('Ingrese el tamaño de la red cristalina\nL = '))

#   crear los bucles para las 3 sumas
#   cada suma varía una coordenada (i,j,k)

for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            
            #   la suma se efectúa sobre toda la red excepto en el origen
            #   luego se ejecuta para los valores en los que i, j y k son
            #   distintos de cero
            
            if (i != 0 and j != 0 and k != 0):
                
                #   variar los valores +1 o -1 considerando si
                #   i+j+k es par o impar
                
                M += ((-1)**(i+j+k))/sqrt((i**2) + (j**2) + (k**2))

print(f'Para L = {L:1.0e}  ->  M = {M:1.3f}')

fin = time()

print(f'Tiempo de ejecución: {fin-inicio: 3.4f} s')