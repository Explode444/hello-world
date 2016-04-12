import re
 
print sum( [int(x) for x in re.findall('[0-9]+', open("C:\Users\jordan.frank\Desktop\python\Class\Week 2\\regex_sum_247360.txt", 'r').read())])