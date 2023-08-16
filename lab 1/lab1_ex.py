#lab1
import time
def FindGCD1(m,n):
    m=abs(m)
    n=abs(n)
    if m==0:
        return n
    if n==0:
        return m
    if m < n: # find min, can use t = min(n,m)
        t = m 
    else:
        t = n
    while True:
        if m % t == 0:
            if n % t == 0:
                return t
        t = t-1

def FindGCD2(m,n): # factorization
    fact1 = [] #find the prime factorization of m
    fact2 = [] #find the prime factorization of n
    m=abs(m)
    n=abs(n)
    if m==0:
        return n
    if n==0:
        return m
    if m==1 or n==1:
        return 1
    i = 2
    j = 2
    while i <= m:     
        if m % i==0:      
            fact1.append(i)
            m = m//i
        else:
            i += 1
    while j <= n:
        if n % j==0:      
            fact2.append(j)
            n = n//j
        
        else:
            j += 1     
    # find all common prime factors
    gcd = 1
    n = 0
    for i in range(len(fact1)):
        for j in range(n,len(fact2)):
            if fact1[i] == fact2[j]:
                gcd = gcd*fact1[i] # product of all common prime factors
                n+=1
                break
    return gcd
            
def FindGCD3(m,n): # recursive
    m=abs(m)
    n=abs(n)
    if m==0:
        return n
    if n==0:
        return m
    t1 = 1
    if m > n:
        t1 = FindGCD3(m%n,n) 
    elif m == n:
        t1 = m
    elif m < n:
        t1 = FindGCD3(m,n%m)  
    return t1


f = open("Extra Case3.txt","r")  
for i in f:
    i = i.split(",")
    print("GCD1")
    
    print(FindGCD1(int(i[0]),int(i[1])))
    
    print("GCD2")
    
    print(FindGCD2(int(i[0]),int(i[1])))
    print(time.time_ns() - t0)
    print("GCD3")
    t0 = time.time_ns()
    print(FindGCD3(int(i[0]),int(i[1])))
    print(time.time_ns() - t0)
f.close()

