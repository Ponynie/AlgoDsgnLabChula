import timeit
import matplotlib.pyplot as plt
#import pandas as pd

def FindGCD1(m: int, n: int) -> int:
    #*GCD(m, n) == GCD(|m|, |n|) for any number, GCD(0, 0) == 0, GCD(a, 0) == |a|
    m, n = abs(m), abs(n)
    if m == 0 and n == 0:
        return 0
    elif m == 0 : 
        return n
    elif n == 0 : 
        return m
    
    #?Naive-prime-factorization-------------------------------------------------------------
    def naive_prime_factors(n: int) -> list:
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

def FindGCD2(m: int, n: int) -> int:
    #*GCD(m, n) == GCD(|m|, |n|) for any number, GCD(0, 0) == 0, GCD(a, 0) == |a|
    m, n = abs(m), abs(n)
    if m == 0 and n == 0:
        return 0
    elif m == 0 : 
        return n
    elif n == 0 : 
        return m
    
    #?Sieve-of-Eratosthenes-function------------------------------------------------------------
    def sieve_of_eratosthenes(n: int) -> int:
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
    def sieve_prime_factors(n: int) -> int:
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
    
def FindGCD3(m: int, n: int) -> int:
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

#?For-accept-multiple-parameters-----------------------------------------------------------------
def multiple_parameters_GCD(gcd_func: callable, gcd_list: list) -> int:
    if len(gcd_list) == 2:
        return gcd_func(gcd_list[0], gcd_list[1])
    else:
        small_gcd_list = []
        i, j = 0, 1
        while j < len(gcd_list):
            small_gcd_list.append(multiple_parameters_GCD(gcd_func, gcd_list[i:j+1]))
            i += 1
            j += 1
        return multiple_parameters_GCD(gcd_func, small_gcd_list)
    
#?Time-recorder-and-input-file-------------------------------------------------------------------
times_gcd1 = []
times_gcd2 = []
times_gcd3 = []
line_count = 0
print("--------------------------------------------")

file_path = "lab 1/Extra Case1.txt" #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< INPUT FILE PATH HERE !!!!!!!!!!!

with open(file_path, "r") as file:
    for line in file:
        input_list = list(map(int, line.strip().split(",")))
        times_gcd1.append(timeit.timeit("multiple_parameters_GCD(FindGCD1, input_list)", globals=globals(), number=1))
        print(f"GCD1-Naive of {tuple(input_list)} is {multiple_parameters_GCD(FindGCD1, input_list)}")
        times_gcd2.append(timeit.timeit("multiple_parameters_GCD(FindGCD2, input_list)", globals=globals(), number=1))
        print(f"GCD2-Sieve of {tuple(input_list)} is {multiple_parameters_GCD(FindGCD2, input_list)}")
        times_gcd3.append(timeit.timeit("multiple_parameters_GCD(FindGCD3, input_list)", globals=globals(), number=1))
        print(f"GCD3-Eucli of {tuple(input_list)} is {multiple_parameters_GCD(FindGCD3, input_list)}")
        line_count += 1
        print("--------------------------------------------")
'''       
#?Export-to-csv-in-microsec------------------------------------------------------------------------    
data = pd.DataFrame({"Naive GCD1": times_gcd1, "Sieve GCD2": times_gcd2, "Eucli GCD3": times_gcd3})
data = data * 10**6
data.to_csv("lab 1/GCD_time_execution.csv")
'''
#?Graph-plot---------------------------------------------------------------------------------------
x_axis = [i + 1 for i in range(line_count)]
fig, ax = plt.subplots()
ax.plot(x_axis, times_gcd1, color = "green", label = "GCD1")
ax.plot(x_axis, times_gcd2, color = "red", label = "GCD2")
ax.plot(x_axis, times_gcd3, color = "blue", label = "GCD3")
ax.set_title("GCD Execution Time")
ax.set_xlabel("Input Sequences")
ax.set_ylabel("Execution Time")
#ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.7f}'))
ax.grid(True)
ax.legend()
plt.show()


            
            
