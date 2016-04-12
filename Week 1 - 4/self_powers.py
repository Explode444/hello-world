import time
sum = 0
start = time.time()
for num in range(1,1001):
    sum += num ** num
    
print str(sum)[-10:]
print time.time() - start

def is_prime(num):
    return all(num % i for i in range(2, int(num**.5 + 1)))
    
print is_prime(8)
print is_prime(7)    