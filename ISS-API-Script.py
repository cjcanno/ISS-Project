import urllib3
import json

http = urllib3.PoolManager() #Required for urllib3 to open URLS

req = http.request('GET', "http://api.open-notify.org/iss-now.json")

data = json.loads(req.data.decode('utf-8')) #Takes the data from urllib3 and loads into json

for key, value in data.items(): #goes over each KVP and prints
    print(key, value, sep=':')
