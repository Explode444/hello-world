f = open("C:\Users\jordan.frank\Desktop\python\Class\Week 1 - 4\p022_names.txt")
data = sorted(f.read().split(","))
names = []
for line in data:
    line = line.replace('"',"")
    names.append(line)

    
for num in range(len(names)):
    val = 0
    for chr in names[num]:
        #print chr, ord(chr) - 64
        val += ord(chr) - 64
    data[num] = val

val = 0
for num in range(len(names)):
    val += (num+1) * data[num]

# print data[0], names[0]
# print data[1], names[1]    
print val
    
