import euler, time
start = time.time()

prime_list = [x for x in euler.prime_sieve(1000)]
print prime_list

# max_primes = 0
# for a in range(-1001, 1000, 2):
    # for b in prime_list:
        # n = 0
        # while euler.is_prime(n**2 + a * n + b):
            # n += 1
        # if n > max_primes:
            # print "a:", a, "b:", b, "n:", n
            # max_primes = n
# print "calculated in", time.time() - start
for prime in prime_list[::-1]:
    if (10**(prime - 1) - 1) % prime == 0:
        print prime
        break