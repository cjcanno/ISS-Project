import urllib3
import json
import requests
from pprint import pprint
from variables import *

http = urllib3.PoolManager()  #Required for urllib3 to open URLS

req = http.request('GET', "http://api.open-notify.org/iss-now.json")

data = json.loads(req.data.decode('utf-8')) #Takes the data from urllib3 and loads into json

for key, value in data.items(): # goes over each KVP and prints
    print(key, value, sep=':')

webex_data = json.dumps(data)
#######################Begin Webex Requirements##############

ACCESS_TOKEN = '' ## use webex token here
roomID = '' # Insert webex room here

def SetHeaders():
    accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
    spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    return (spark_header)


def postMsg(the_header, message):
    message = {"roomId":roomID,"text":message}
    url = 'https://webexapis.com/v1/messages'
    resp = requests.post(url, json=message, headers=the_header)
    print('message sent to server')
    print("postMsgJSON ", resp.json())


header = SetHeaders()
postMsg(header, webex_data)

