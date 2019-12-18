def fib(n):
    '''Compute the nth term of fibonacci sequence'''
    # First Fibonacci number is 0 
    if n == 0: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 1: 
        return 1
    else: 
        return fib(n-1) + fib(n-2)