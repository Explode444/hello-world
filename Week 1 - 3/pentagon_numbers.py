import time
def pentagon(n):
    return n * (3 * n - 1) / 2
start = time.time()
# #build array
# numbers = [pentagon(x) for x in range(1, 10000)]    

# for num in range(len(numbers)):
    # for sec_num in numbers[num:]:
        # if numbers[num] != sec_num:
            # if numbers[num] + sec_num in numbers and sec_num - numbers[num] in numbers:
                # print numbers[num], sec_num, sec_num - num
    # print "Elapsed time", time.time() - start, "seconds"
# print "None"
ps = set()
i = 0
while True:
    i += 1
    p = pentagon(i)
    ps.add(p)
    for n in ps:
        if p-n in ps and p-2*n in ps:
            print p-2*n