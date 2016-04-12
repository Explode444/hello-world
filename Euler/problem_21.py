from euler import factors, is_prime

def remove_last(func):
    def wrapper(*args):
        s = func(*args)
        if is_prime(args[0]):
            return set([1])
        return s.difference(args)
    return wrapper

def sum_it(val):
    if len(val) < 2:
        return 1
    return reduce(lambda x, y: x+y, val)
    
factors = remove_last(factors) 
# print sorted(factors(220))
# print reduce(lambda x, y: x+y, sorted(factors(220)))
# print reduce(lambda x, y: x+y, sorted(factors(284)))
sum = 0
for num in range(2, 10000):

    a = sum_it(factors(num))
  #  print a
  #  print factors(a)
    b = sum_it(factors(a))
   # print b
    if num == b and num != a:
        print "here", num
        sum += num
print "the answer is: ", sum