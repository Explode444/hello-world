import itertools
digits = [(1,4,2), (2,5,3), (3,6,5), (4,7,7), (5,8,11), (6,9,13), (7,10,17)]
p = 9
ps = '0123456789'[:p+1]

s = 0
for px in itertools.permutations(ps, p+1):

	q = ''.join(px)
	qs = 0
	for d in digits[:p-2]:
		qs+= int(q[d[0]:d[1]]) % d[2]
	if qs==0: s+= int(q)

print s