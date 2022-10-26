import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print('timestamp')
print('iss_position','latitude','data','iss_position','latitude')
