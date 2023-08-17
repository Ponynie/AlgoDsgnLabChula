import timeit
import matplotlib.pyplot as plt

def FindGCD1(m, n):
    #*GCD(m, n) == GCD(|m|, |n|) for any number, GCD(0, 0) == 0, GCD(a, 0) == |a|
    m, n = abs(m), abs(n)
    if m == 0 and n == 0:
        return 0
    elif m == 0 : 
        return n
    elif n == 0 : 
        return m
    #?Naive-prime-factorization-------------------------------------------------------------
    def naive_prime_factors(n):
        factors = [1]
        divisor = 2
        while n > 1:
            if n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            else:
                divisor += 1
        return factors
    
    prime_factors_m = naive_prime_factors(m)
    prime_factors_n = naive_prime_factors(n)
    
    #?Calculate-product-of-common-prime-factors-----------------------------------------------
    product_common = 1
    m_idx, n_idx = 0, 0
    while m_idx < len(prime_factors_m) and n_idx < len(prime_factors_n):
        if prime_factors_m[m_idx] == prime_factors_n[n_idx]:
            product_common *= prime_factors_m[m_idx]
            m_idx += 1
            n_idx += 1
        elif prime_factors_m[m_idx] > prime_factors_n[n_idx]:
            n_idx += 1
        elif prime_factors_m[m_idx] < prime_factors_n[n_idx]:
            m_idx += 1
    
    return product_common #Return product of common as GCD(m, n)

def FindGCD2(m, n):
    #*GCD(m, n) == GCD(|m|, |n|) for any number, GCD(0, 0) == 0, GCD(a, 0) == |a|
    m, n = abs(m), abs(n)
    if m == 0 and n == 0:
        return 0
    elif m == 0 : 
        return n
    elif n == 0 : 
        return m
    
    #?Sieve-of-Eratosthenes-function------------------------------------------------------------
    def sieve_of_eratosthenes(n):
        prime = [True] * (n + 1)
        prime[0] = prime[1] = False
        
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        
        return [i for i in range(2, n + 1) if prime[i]]
    
    #?Sieve-optimized-prime-factorization--------------------------------------------------------
    def sieve_prime_factors(n):
        primes = sieve_of_eratosthenes(n)
        factors = []
        
        for prime in primes:
            while n % prime == 0:
                factors.append(prime)
                n //= prime
            if n <= 1: break
        return factors
    
    prime_factors_m = sieve_prime_factors(m)
    prime_factors_n = sieve_prime_factors(n)
    
    #?Calculate-product-of-common-prime-factors-----------------------------------------------
    product_common = 1
    m_idx, n_idx = 0, 0
    while m_idx < len(prime_factors_m) and n_idx < len(prime_factors_n):
        if prime_factors_m[m_idx] == prime_factors_n[n_idx]:
            product_common *= prime_factors_m[m_idx]
            m_idx += 1
            n_idx += 1
        elif prime_factors_m[m_idx] > prime_factors_n[n_idx]:
            n_idx += 1
        elif prime_factors_m[m_idx] < prime_factors_n[n_idx]:
            m_idx += 1
    
    return product_common #Return product of common as GCD(m, n)
    

def FindGCD3(m, n):
    #*GCD(m, n) == GCD(|m|, |n|) for any number, GCD(0, 0) == 0, GCD(a, 0) == |a|
    m, n = abs(m), abs(n)
    if m == 0 and n == 0:
        return 0
    elif m == 0 : 
        return n
    elif n == 0 : 
        return m
    
    #?Call-recursive-----------------------------------------------------------------------------
    if m > n:
        return FindGCD3(m % n, n)
    elif m < n:
        return FindGCD3(m, n % m)
    else:
        return m 


input = (100, 36)
print(FindGCD1(input[0], input[1]))
print(FindGCD3(input[0], input[1]))
