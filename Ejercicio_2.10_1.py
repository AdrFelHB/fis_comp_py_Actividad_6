#!/usr/bin/env python3
"""
    Propósito:  calcular la energía de ligaduray energía de ligadura
                por nucleón dados A y Z.
    Ejercicio 2.10 del libro de Mark newman, Computational Physics.
    Autor: Adrián Hernández.
    Fecha: 3 de octubre de 2021.
"""

from numpy import *

#   ingreso de  A y Z

Z = int(input('Ingrese el número atómico\nZ = '))
A = int(input('Ingrese el número de masa\nA = '))

#   declaración de constantes a1, a2, a3, a4 en eV

a1 = 15.8
a2 = 18.3
a3 = 0.74
a4 = 23.2

#   declarar constante a5 a partir de A y Z

if (A%2) != 0:
    a5 = 0
elif (A + Z)%2 == 0:
    a5 = 12.0
elif (A + Z)%2 != 0:
    a5 = -12.0
    
#   cálculo de la energía de ligadura B

B = a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) -a4*(((A - 2*Z)**2)/(A)) + a5/(A**(1/2))

print(f'\nPara Z = {Z:3d} y A = {A:3d} la energía de ligadura es\nB = {B:3.3f} MeV\n')

#   cálculo de la energía de ligadura por nucleón

B_n = B/A
print(f'Para Z = {Z:3d} y A = {A:3d} la energía de ligadura por nucleón es\nB/A = {B/A:3.3f} MeV')
