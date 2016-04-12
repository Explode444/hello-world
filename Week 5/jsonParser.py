import urllib
import json

url = "http://python-data.dr-chuck.net/comments_247366.json"
f = urllib.urlopen(url)
data = json.loads(f.read())

sum = 0
for item in data["comments"]:

    sum += item["count"]
    
print sum
