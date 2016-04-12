import urllib2
url = "https://projecteuler.net/project/resources/p079_keylog.txt"

f = urllib2.urlopen(url)
data = f.readlines()

digits = set()

for line in data:
    digits.add((int(line[0]), int(line[1]), int(line[2])))

d = {0: set(),
1: set(),
2: set(),
3: set(),

6: set(),
7: set(),
8: set(),
9: set()
}

for spot in digits:
    d[spot[0]].add(spot[1])
    d[spot[0]].add(spot[2])
    d[spot[1]].add(spot[2])

for k in sorted(d, key=lambda k: len(d[k]), reverse=True):
    print k,

    
#print d.sort(key=len, reverse=True)