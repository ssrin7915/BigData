import oauth2
import os
import json
import urllib

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    lines=f.readlines()
    for line in lines:
        row=line.split('=')
        row0=row[0]
        d[row0] =row[1].strip()
    return d

keyPath=os.path.join(os.getcwd(),'src','key.properties')

key=getKey(keyPath)

consumer = oauth2.Consumer(key=key['api_key'], secret=key['api_secret'])
token=oauth2.Token(key=key['access_token'], secret=key['access_secret'])
client = oauth2.Client(consumer,token)
url= "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Write Hello 20161113'})
response,content = client.request(url,method='POST',body=mybody)
