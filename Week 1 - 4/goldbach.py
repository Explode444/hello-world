# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
import time
start = time.time()
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
            del D[q]
        
        q += 1    

def check_gold(num, square, prime):
    if num == prime + 2 * square:
            return True
    return False

def next_num(num, prime_list):
    num += 2
    while num in prime_list:
        num+=2
    return num    

def main():    
    primes = gen_primes()
    squares_list = [x ** 2 for x in range(1, 50)]
    prime_list = [primes.next() for dummy_x in range(1000)]
    #print prime_list
    num = 9     


    def cycle(num, prime_list, squares_list):
        for prime in prime_list:
            for square in squares_list:
                if check_gold(num, square, prime):
                    print "Checked: %i = %i + 2 x %i" %(num, prime, square)
                    return True
                
        return False
    while cycle(num, prime_list, squares_list):
        num = next_num(num, prime_list)                
                    
    print "Failed:", num
    print "Run time %f seconds" %(time.time() - start)

if __name__ == "__main__":
    main()