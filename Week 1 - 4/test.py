# n = 5
# f = 1
# primes = set()
 
# while True:
    # if all(n % p for p in primes):
        # primes.add(n)
    # else:
        # if not any((n-2*i*i) in primes for i in range(1, n)):
            # break
    # n += 3-f
    # f = -f

# print "Project Euler 46 Solution =", n

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        print "q:", q
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
                print "p", p
                print "this is d", D
            del D[q]
        
        q += 1         
prime = gen_primes()
for x in range(10):
    print prime.next()