import re

str = "From stephen.marquard@uct.ac.za Sat $Jan  5 09:14:16 2008"
ans = re.findall('\S+?@\S+', str)
print ans


x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print y