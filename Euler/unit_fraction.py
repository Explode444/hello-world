def memoize(f):
    memo = {}
    def helper(gx):
        if gx not in memo:            
            memo[gx] = f(gx)
        return memo[gx]
    return helper
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
#fib = memoize(fib)
val = 0
count = 0
while len(str(val)) < 1000:
    val = fib(count)
    count += 1
print count -1
