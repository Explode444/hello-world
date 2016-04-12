from goldbach import gen_primes
import time

factors = {}
start = time.time()
primes = gen_primes()
prime_list = []
for dummy_x in range(100000):
    prime = primes.next()
    prime_list.append(prime)
    inc = 1
    while inc * prime < 1000050:
        if inc * prime in factors:
  #          print "here"
            factors[inc * prime].append(prime)
        else:
 #           print "or here"
            factors[inc * prime] = [prime]
        inc += 1
istrue = True
while istrue:
    for val in factors:
        if len(factors[val]) > 3 and len(factors[val + 1]) > 3 and len(factors[val + 2]) > 3 and len(factors[val + 3]) > 3:
            print val, factors[val]
            print val + 1, factors[val+1]
            print val + 2, factors[val+2]
            print val + 3, factors[val+3]
            istrue = False
            break
