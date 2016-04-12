import re 

loc = "C:\Users\jordan.frank\Desktop\python\Class\Week 2\\"
file = "regex_sum_247360.txt"
f = open(loc + file, "r")

values = []

data = f.read()

lst = re.findall("[0-9]+", data)

total = 0       
for val in lst:
    total += int(val)

print total    
    