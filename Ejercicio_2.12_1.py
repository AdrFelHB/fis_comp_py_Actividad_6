#!/usr/bin/env python3

from numpy import sqrt, size

def numeros_primos(N):
    n_primo = [2]
    n = 3 

    while n<= N:
        for k in range(0,size(n_primo)):
            if (n%sqrt(n) == 0) or (n%n_primo[k] == 0):
                break
            else:
                n_primo.append(n)
                break
        n += 1
    for k in n_primo:
        print(k)

numeros_primos(10000)
