from goldbach import gen_primes
import time

start = time.time()
def euler(limit):
    primes = gen_primes()
    prime = 2
    prime_list = []
    cumulative_sum = [2]
    while prime < limit:
        prime = primes.next()
        prime_list.append(prime)
    prime_list.pop()
    return prime_list
    
def main():
    limit = 1000000
    primes = euler(limit)
    largest = 0
    chain = []
    for start in range(10):
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > limit:
                break
            i += 1
            if total in primes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    print(sum(chain))

if __name__ == "__main__":
    main()