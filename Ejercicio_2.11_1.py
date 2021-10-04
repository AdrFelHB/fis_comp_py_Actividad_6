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

def triangulo_pascal(L):
    for n in range(0,L):
        linea = []

        for k in range(0,n+1):
            linea.append(coeficiente_binomial(n,k))
        
        print(linea)
        print("")
        
triangulo_pascal(20)

