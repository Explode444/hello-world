import itertools
import time
start = time.time()
primes = [2, 3, 5, 7, 11, 13, 17]
str = '1406357298'
pandigitals = list(map("".join, itertools.permutations(str)))
sum = 0


def check_digits(number):
    for digit in range(1, len(str)-2):
        if int(number[digit:digit+3]) % primes[digit - 1] != 0:
            return False
    return True
    
for number in pandigitals:
    if check_digits(number):
        sum +=int(number)
print sum, time.time()-start