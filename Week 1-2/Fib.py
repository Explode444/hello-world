def fib(num):
    if num <= 0:
        return 0
    if num == 1:
        return 1
    if num % 2 == 1:
        return fib(num-2) + fib(num-1)
    else:
        return fib(num-1)
        
print fib(100)