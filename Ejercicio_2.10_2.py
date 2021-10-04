#!/usr/bin/env python3
"""
    Propósito:  calcular la energía de ligaduray energía de ligadura
                por nucleón dados A y Z.
    Ejercicio 2.10 del libro de Mark newman, Computational Physics.
    Autor: Adrián Hernández.
    Fecha: 3 de octubre de 2021.
"""

from numpy import *

#   ingreso de  Z 

Z = int(input('Ingrese el número atómico\nZ = '))

#   declaración del número de masa como un arreglo entre Z y 3Z

A = list(range(Z,3*Z + 1))

#   declaración de el arreglo para la energía de ligadura por nucleón
#   para cada número de masa A.

B_n = list(zeros(shape(A)))

#   declaración de constantes a1, a2, a3, a4 en eV

a1 = 15.8
a2 = 18.3
a3 = 0.74
a4 = 23.2



for k in range(0,size(A)):
    
    #   declarar constante a5 a partir de A y Z

    if (A[k]%2) != 0:
        a5 = 0
    elif (A[k] + Z)%2 == 0:
        a5 = 12.0
    elif (A[k] + Z)%2 != 0:
        a5 = -12.0
    
    #   cálculo de la energía de ligadura por nucleón B/A
    
    B_n[k] = a1*A[k] - a2*(A[k]**(2/3)) - a3*((Z**2)/(A[k]**(1/3))) -a4*(((A[k] - 2*Z)**2)/(A[k])) + a5/(A[k]**(1/2))
    B_n[k] = B_n[k]/A[k]

#   encontrar el núclo más estable, es decir la energía de ligadura por 
#   nucleón más alta

most_stable = B_n.index(max(B_n))

print(f'\nPara Z ={Z:3d}, el cálculo más estable es con A = {A[most_stable]:3d} que da la energía de ligadura por nucleón\nB = {B_n[most_stable]:3.3f} MeV\n')


#   cálculo de la energía de ligadura por nucleón

#B_n = B/A
#print(f'Para Z = {Z:3d} y A = {A:3d} la energía de ligadura por nucleón es\nB/A = {B/A:3.3f} MeV')