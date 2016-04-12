import euler

prime_list = [x for x in euler.prime_sieve(1000000)]

def rotate_left(num):
    num = str(num)
    first_digit = num[0]
    return num[1:] + first_digit

#euler.is_prime(rotate_left(prime))
def check_prime(num):
    length = len(str(num))
    inc = 1
    while inc < length:
        num = rotate_left(num)
        if not euler.is_prime(int(num)):
            return False
        inc += 1
  #  print num
    return True
        
answer = []    
count = 0
for prime in prime_list:
    if check_prime(prime):
        count += 1
        answer.append(prime)
print count
print answer
    