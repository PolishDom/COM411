import json
import requests

data = {
    "name": "Prins",
    "job": "Lecturer"
}

json_data = json.dumps(data)
requests.post("https://somesite.com/post", json=json_data)


################################################################


import requests

response = requests.get("https://somesite.com/data.json")
print(response.json())