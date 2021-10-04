def factorial(k):
    if k > 1:
        return k * factorial(k-1)
    elif (k==1) | (k==0):
        return 1
    else:
        print("Error: El número ingresado debe ser no negativo")
    
    
def coeficiente_binomial(n,k):
    out = int( factorial(n) / (factorial(k) * factorial( n - k )))
    return out

def moneda(n,k):
    probabilidad = 100 * coeficiente_binomial(n,k) / (2**n)
    return probabilidad
    

n = int(input('Ingrese el número de lanzamientos\nn = '))
k = int(input('Ingrese el número de veces que saldrá una de las caras de la moneda\nk = '))
probabilidad = moneda(n,k)

print(f'\nLa probabilidad de lanzar la moneda {n:1d} veces\ny que salga una de sus caras {k:1d} es {probabilidad:1.3f} %\n')


print(f'\nLa probabilidad de lanzar una moneda {n:1d} veces y que salga una de sus caras más de {k:1d} veces varía desde {moneda(n,n):1.3f} % hasta {moneda(n,k):1.3f} %')
    
    