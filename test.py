
import requests
import json

while True:
  message = {
    "ToUserName": "gh_919b00572d95", 
    "FromUserName": "oVneZ57wJnV-ObtCiGv26PRrOz23",
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