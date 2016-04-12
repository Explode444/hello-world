import urllib
import json


address = "Matematicki fakultet Beograd"
url = "http://python-data.dr-chuck.net/geojson?"
url = url + urllib.urlencode({"sensor": "false", "address": address})
print url
f = urllib.urlopen(url)
data = f.read()

try: js = json.loads(str(data))
except: js = None

place_id = js["results"][0]["place_id"]
#print json.dumps(place_id, indent=4)
print place_id

