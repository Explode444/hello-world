from goldbach import gen_primes
import time
from itertools import permutations

start = time.time()
primes = gen_primes()
prime_list = []
for dummy_x in range(10000):
    prime_list.append(primes.next())
    
#print prime_list[:15]

for num in range(1000, 9999):
    perms = map("".join, permutations(str(num)))
    perms = sorted(set(map(int, perms)))
    for first_num in perms:
        if first_num in prime_list:
            for sec_num in perms:
                if sec_num in prime_list:
                    diff = sec_num - first_num
                    if diff > 1000:
                        if first_num + diff * 2 in perms and first_num + diff * 2 in prime_list:
                            print "Solution:", first_num, sec_num, sec_num + diff, diff

  #  print perms
print "Completed in %f"  %(time.time() - start)
