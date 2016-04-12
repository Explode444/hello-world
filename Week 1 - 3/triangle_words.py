import urllib2, time
url = "https://projecteuler.net/project/resources/p042_words.txt"

f = urllib2.urlopen(url).read().replace('"', "").split(",")
start = time.time()
triangle_list = [n*(n+1) / 2 for n in range(1,100)]
#print triangle_list
#print ord('Z')-64
#print ord('A')-64
count = 0
for word in f:
    sum = 0
    for letter in word:
        sum += ord(letter) - 64
    if sum in triangle_list:
        count += 1
print "There are %i triangle words in the list.  Foud in %f seconds" %(count, time.time() - start)