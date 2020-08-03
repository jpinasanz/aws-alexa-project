import sys
from xml.dom import minidom
import requests

import base64
import json
base = "itsstaff:4%oypcI0"

# Standard Base64 Encoding
encodedBytes = base64.b64encode(base.encode("utf-8"))
encodedStr = str(encodedBytes)

def send(manifestPath,srtPath):
    #print("sending " + srtPath +" to "+manifestPath)
    #f = open(manifestPath, "r")
    #print(f.read())
    #get callback url
    xmldoc = minidom.parse(manifestPath)
    itemlist = xmldoc.getElementsByTagName('CallbackURL')
    uri=itemlist[0].firstChild.nodeValue
    #set up authentication info for call
    headers={
       "Host" : "mediasite.sdsu.edu",
       #"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
       "sfapikey" : "0f909c4d-e843-4879-9e04-452ac2f7d257",
       #"Accept-Encoding" : "gzip,deflate,sdch",
       #"Accept-Language" : "en-US,en;q=0.8",
       "Authorization": "Basic "+encodedStr
     }
    #do post request with file from srt path
    files = {'c65ba9cb-dafd-4521-9e15-d28060cdba2a.srt': open(srtPath, 'rb')}
    data=open(srtPath, 'r').read()
    print(files)
    response = requests.post(uri,headers=headers, data=data)
    print(response)
    print(response.text)

#takes command line input or uses default when called
if __name__ == "__main__":

    if len(sys.argv)>1:
        send(sys.argv[1],sys.argv[2])
    else:
        send("/home/sftp_user/"+"5ca07435-63c8-47c2-b845-0c20a1452963.manifest","/home/ec2-user/testfolder/NewSRTFile.srt")
