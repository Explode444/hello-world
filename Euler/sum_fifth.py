def check_sum_power(num, p=5):
    sum = 0
    num = str(num)
    for digit in num:
        sum += int(digit) ** p
    if sum == int(num):
        return True
    else:
        return False
sum = 0
for num in range(2, 6*9**6):
    if check_sum_power(num):
        print num
        sum += num
print "The sum is:", sum