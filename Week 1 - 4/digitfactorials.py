import time
start = time.time()


def is_palindrome(str_check):
    str_check = str(str_check)
    num = 1
    if str_check(n) != str_check(n)[::-1]:
        return False
        num += 1    
    return True
sum = 0  
for num in range(1, 1000000, 2):
    if is_palindrome(num):
        binary = bin(num)[2:]
        if is_palindrome(binary):
            sum += num
print sum
print time.time() - start