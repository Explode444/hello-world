import euler
sum = 0
count = 0                
prime_list = [x for x in euler.primes_sieve(1000000)]

def trunc_prime(prime): 
    prime = str(prime)
    for num in range(1, len(prime)):
        if not euler.is_prime(int(prime[num:])) or not euler.is_prime(int(prime[:-num])):
            return False
    return True  

for prime in prime_list[4:]:
    if trunc_prime(prime):
        count += 1
        sum += prime
        print prime

print count, sum