'''
En este código se detalla como se logra sacar la secuencia de 
fibonacci entendida f(n) = f(n - 1) - f(n - 2)
'''

def fibonacci(n):
    if n == 0: 
        return 0
    
    elif n == 1: 
        return 1 
    
    else: 
        return fibonacci(n-1) + fibonacci (n-2)
    
n = 100
print(fibonacci(n))   