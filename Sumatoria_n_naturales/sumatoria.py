#Hacer una sumatoria de los números naturales usando la recursividad.
# Formula FUNCION(N) = N + FUNCION(N) si n != 0 o n != 1 

def sumatoria(n): 
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return n + sumatoria(n - 1)
    
n = 10
print(sumatoria(n))
