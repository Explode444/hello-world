def memoize(func):
    mem = {}
    def wrapper(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapper

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_pandigital(n, s=9): 
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)
    
def prime_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
#Use like this              
#prime_list = [x for x in primes_sieve2(1000000)]

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True