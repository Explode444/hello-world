import euler
prime = '29'
def trunc_prime(prime): 
    prime = str(prime)
    for num in range(1, len(prime)):
        print int(prime[num:]), int(prime[:num])
        if not euler.is_prime(int(prime[num:])) or not euler.is_prime(int(prime[:-num])):
            return False
    return True  
print trunc_prime(prime)