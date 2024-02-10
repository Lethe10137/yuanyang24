
import requests
import json


import base64
import binascii

# i = "a007062b4c1a997ccb5558d20c0a28e4f419d41a8c"

# i = "a007062b4e2e1e8199a24b7d3ac841501e1c044a28"

# i = "a007062b4fe7df6dab7ac1e974524573437c0c549c"

i = "a007062b4f83f1ba1dd2f8e683850e45310c32adf8"

wxid = base64.b64encode(binascii.unhexlify(i)).decode()

print(wxid)


while True:
  message = {
    "ToUserName": "gh_919b00572d95", 
    "FromUserName": wxid,
    "CreateTime": 1651049934,
    "MsgType": "text", 
    "Content": input(), 
    "MsgId": 23637352235060880 
  }

  result = requests.post(
      "http://127.0.0.1:8000/reply/",
      json = message
  )

  print(result.content.decode())
  
  print(json.loads(result.content.decode())["Content"])