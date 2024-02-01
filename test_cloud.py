
import requests
import json


message = {
  "action": "load", 
  "openid": "a159de679ef026757e39bb42886bf6e8f46b3b3db7",
  # "token": "af58d2b608c5fc700bab6309140e2eef9b5eb7063d4c8cd583b5044d58f6acdf4db3d16a137b87489a0f8401c5028b7ccc03f2a7e9a59a9079dd2d9407117549"
  "token" : "39656836"
}

result = requests.post(
    "http://127.0.0.1:8000/cloud/",
    json = message
)

print(result.content.decode())

print(json.loads(result.content.decode()))