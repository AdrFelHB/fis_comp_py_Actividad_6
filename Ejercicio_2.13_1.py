#! /usr/local/bin/python

def catalan(n):
    if n > 0:
        return catalan(n-1) * ((4*n - 2)/(n + 1))
    elif n == 0:
        return 1
    else:
        print('Error: Ingrese un número no negativo')

n = int(input('Ingrese un entero no negativo\nn = '))

print(f'El número de Catalan C{n} es {catalan(n):1.3e}')
