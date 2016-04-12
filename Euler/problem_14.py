#Problem 14

def collatz(num, depth=0):
    if num < 2:
        
        return depth + 1
        
    if num % 2 == 0:
        return collatz(num/2, depth = depth + 1)
    else:
        return collatz(3 * num + 1, depth = depth + 1)

max = 0
val = 0
for num in range(1, 1000000):
    if collatz(num) > max:
        max = collatz(num)
        val = num
print max, "value:", val