def longest_prime_sum(limit):
    """Return the prime below limit that can be written as as the sum of
    the most consecutive primes.

    >>> longest_prime_sum(100)
    41

    """
    prime_list = list(primes(end=limit))
    prime_set = set(prime_list)

    # Find max number of consecutive primes whose sum is below limit.
    total = 0
    for max_length, p in enumerate(prime_list):
        total += p
        if total >= limit:
            break

    for length in range(max_length + 1, 0, -1):
        for x in range(len(prime_list) - length + 1):
            total = sum(prime_list[x:x+length])
            if total >= limit:
                break
            elif total in prime_set:
                return total
print longest_prime_sum(100)