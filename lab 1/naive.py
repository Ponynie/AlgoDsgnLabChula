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


num = int(input("Enter a number: "))
factors = naive_prime_factors(num)

if len(factors) == 0:
    print(f"{num} has no prime factors.")
else:
    print(f"The prime factors of {num} are: {factors}")