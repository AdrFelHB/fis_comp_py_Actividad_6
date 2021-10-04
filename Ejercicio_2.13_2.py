#! /usr/local/bin/python

#definir función que calcule el máximo compun divisor de dos números

def mcd(m,n):
    if n == 0:
        return m
    elif n > 0:
        return mcd(n,m%n)
    else:
        print('Ingrese un entero no negativo')

m = int(input('Ingrese un entero positivo\nm = '))
n = int(input('Ingrese un entero positivo\nn = '))

print(f'El máximo compun divisor entre {m} y {n} es {mcd(m,n)}')
