def prime_fact(n):
   pfactor = []
   while(n%2==0):
    pfactor.append(2)
    n = n/2
   for i in range(3, n, 2):
    if(n%i==0):
        pfactor.append(i)
        n = n/i
        if(n<=1):
            break
   return pfactor
def gcd1(a,b):
    pf_a = prime_fact(a)
    pf_b = prime_fact(b)
    all_prime_fact = []
    i, j = 0,0
    while i < len(pf_a) and j < len(pf_b):
        if pf_a[i] == pf_b[j]:
            all_prime_fact.append(pf_a[i])
            i += 1
            j += 1
        elif pf_a[i] < pf_b[j]:
            i += 1
        else:
            j += 1
    n = 1
    for factor in all_prime_fact:
        n = factor
    return n

a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(a==0 or b==0):
    print("error")
if(a<0 and b<0):
    a = a(-1)
    b = b(-1)
    print(gcd1(a,b))
elif (a<0):
    a = a(-1)
    print(gcd1(a,b))
elif (b<0):
    b = b*(-1)
    print(gcd1(a,b))