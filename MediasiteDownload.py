import requests

import base64

base = "itsstaff:4%oypcI0"

# Standard Base64 Encoding
encodedBytes = base64.b64encode(base.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

response = requests.get(f"https://mediasite.sdsu.edu/Mediasite/api/v1/Presentations",
 headers={
   "Host" : "mediasite.sdsu.edu",
   "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
   "sfapikey" : "0f909c4d-e843-4879-9e04-452ac2f7d257",
   "Accept-Encoding" : "gzip,deflate,sdch",
   "Accept-Language" : "en-US,en;q=0.8",
   "Authorization": "Basic "+encodedStr
 }
)

#url = 'https://mediasite.sdsu.edu/Mediasite/api/'
#data = '''{
#  
#}'''
#response = requests.post(url, data=data)
one=True
print("status: "+str(response.status_code))
content=response.json()
for value in content['value']:
    if one:
    	print(value)
    one=False
