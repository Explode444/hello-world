import itertools
import sys
import time
sys.path.insert(0, 'C:\Users\jordan.frank\Desktop\python\Class\Week 1 - 4')
from goldbach import gen_primes

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
                
# def is_pandigital(num):
    # num = str(num)
    # for digit in range(len(num) + 1):
        # if num[digit] in num[:digit] or num[digit] in num[digit + 1:]:
            # return False
    # return True
def is_pandigital(n, s=7): 
    n=str(n)
    return len(n)==s and not '1234567890'[:s].strip(n)
# start = time.time()
# primes = gen_primes()
# prime_list = []
# for dummy_x in range(7000000, 7654321):
    # prime = primes.next()
    # print prime
    # prime_list.append(prime)
prime_list = [x for x in primes_sieve2(7654321)]

# num = '7654321'
# permutations = list(map("".join, itertools.permutations(num)))
# print permutations
#sorted_perm = sorted(map(permutations, is_prime))
print "done"
for num in prime_list[::-1]:
    if is_pandigital(num):
        print num
        break

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True




# for num in permutations:
  # #  if '0' not in str(num):
    # if is_prime(int(num)):
        # print "prime:", num
        # if is_pandigital(num):
            # print num

#print is_prime(num)            
