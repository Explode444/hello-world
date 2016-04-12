import urllib2
import xml.etree.ElementTree as ET

url = "http://python-data.dr-chuck.net/comments_247362.xml"
f = urllib2.urlopen(url)

data = f.read()

tree = ET.fromstring(data)

results = tree.findall('.//count')

sum = 0 
for result in results:
    sum += int(result.text)

print sum