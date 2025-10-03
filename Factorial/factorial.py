"""La idea de estos códigos es usar la propiedad de 
recursividad para calcular el factorial de un número. 

factiorial(n) = n * factorial(n-1) si n > 0
factiorial(0) = 1
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
n = 9
print(factorial(n))