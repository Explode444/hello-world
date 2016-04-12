def is_pal(num):

    if str(num) != str(num)[::-1]:
        return False
    return True
    
max_num = float("-inf")  
for i in range(1000):
    for j in range(1000):
        if is_pal(i * j):
            if (i * j) > max_num:
                max_num = i * j

print max_num               