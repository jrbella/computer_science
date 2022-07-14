def factorial(n):
    """Computes and returns the factorial of n, 
    a positive integer.
    """
    if n == 1: # Base cases!
        return 1
    else: # Recursive step
        return n * factorial(n - 1) # Recursive call     

myFactorial = factorial(3)
print(myFactorial)