import math

def SieveOfEratosthenes(n): 
    
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while(p * p <= n): 
    # If prime[p] is not changed, then it is
    # a prime 
        if (prime[p] == True): 
            # Update all multiples of p
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    primes = []

    #adding primes into list
    for p in range(2, n): 
        if prime[p]: 
            primes.append(p)
    return primes

def getDivisors(n):
    # method to get divisors
    divisors = []
    i = 1
    while (i * i < n):
        if (n % i == 0):
            divisors.append(i)
        i += 1
    for i in range(int(math.sqrt(n)), 0, -1):
        if (n % i == 0):
            divisors.append(i)
    return divisors

def solution():
    primes = SieveOfEratosthenes(100000000)
    total = 0

    for prime in primes:
        possible_prime_generating = prime - 1
        divisors = getDivisors(possible_prime_generating)
        short_divisors = divisors[0:int(len(divisors)+1)]
        short_list = primes[0:primes.index(prime)+1]

        for divisor in short_divisors:
            possible_prime = divisor + (possible_prime_generating)/divisor
            if possible_prime not in short_list:
                break
        else:
            total += possible_prime_generating

    print(total)
solution()