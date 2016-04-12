import math
import time

start = time.time()
nums = {}
for p in range(1001):
    nums[p] = []


for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        if c.is_integer():
            p = a + b + c
            if p < 1000:
                nums[p].append((a, b, c))
    
#print nums
# print nums[168]
# print len(nums[168])
max = 0
key = 0
for val in nums:
    if len(nums[val]) > max:
        max = len(nums[val])
        key = val
        
print max, key
print nums[key]
print "Calculated in %f seconds" %(time.time() - start)