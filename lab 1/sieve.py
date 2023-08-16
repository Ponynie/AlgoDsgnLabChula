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

def prime_factors(n):
    primes = sieve_of_eratosthenes(n)
    factors = []
    
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    
    return factors

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    factors = prime_factors(num)
    
    if len(factors) == 0:
        print(f"{num} has no prime factors.")
    else:
        print(f"The prime factors of {num} are: {factors}")
