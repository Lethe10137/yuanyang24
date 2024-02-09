
import requests
import json


# message = {
#   "action": "load", 
#   "openid": "a159de679ef026757e39bb42886bf6e8f46b3b3db7",
#   # "token": "af58d2b608c5fc700bab6309140e2eef9b5eb7063d4c8cd583b5044d58f6acdf4db3d16a137b87489a0f8401c5028b7ccc03f2a7e9a59a9079dd2d9407117549"
#   "token" : "45197524"
# }

message = {
  "action": "submit", 
  "openid": "a159de679ef026757e39bb42886bf6e8f46b3b3db7",
  "token": "e79b43a608196eae93caec566016f669b8a6df7da374d3eecfe00ac011191dc491f175464d73ad604932c5539f83af54afc17bd0bd7cd5ba26708dd7fc23dbcc"
  # "token" : "45197524"
}

# message = {
#     "action": "load",
#     "openid": "a35d68a3ad41f0c358486fdc2a33d5bd66ecdd5294",
#     "token": "83808028",
#     # "a" : "h9uasd87ft8hje2f81829e98asdif8wudhjha"
# }

result = requests.post(
    # "http://127.0.0.1:8000/cloud/",
    # "https://django-bgq6-91011-7-1324104223.sh.run.tcloudbase.com/cloud/",
    # "https://test2.yuanyang.app/cloud/",
    # "http://testapi.yuanyang.app:8080/",
    # "http://8.219.88.123:8080/",
    # "https://back.yuanyang.app/",
    "https://wrapper-mzvnogjrnd.cn-hangzhou.fcapp.run",
    json = message
)

print(result)

print(result.content.decode())

print(json.loads(result.content.decode()))