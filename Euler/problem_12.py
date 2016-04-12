def memoize(func):
    mem = {}
    def wrapper(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapper
# def memoize(f):
    # memo = {}
    # def helper(x):
        # if x not in memo:            
            # memo[x] = f(x)
        # return memo[x]
    # return helper
    
@memoize
def fib(num):
    if num < 2:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


count = 2
sum = 0
val = 0
while val < 4000000:
    val = fib(count)
    if val % 2 == 0:
        sum += val
    count += 1
    
    
print sum