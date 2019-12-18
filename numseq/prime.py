def primes(n):
    '''creates a list of prime numbers up to n'''
    prime_list = []
    for num in range(n):
        if is_prime(num):
            prime_list.append(num)
    return prime_list
                    
                    
def is_prime(n):
    '''returns True if n is a prime number, False if it is not'''
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
