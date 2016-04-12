from itertools import permutations

digits = [x for x in range(10)]
val = []
perms = permutations(digits)
while len(val) < 10:
    val.append(perms.next())
        
print val[(len(val)-1)]
print val