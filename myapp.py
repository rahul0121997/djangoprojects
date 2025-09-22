# import requests
# import json

# URL = "http://127.0.0.1:8080/api/api"


# data = {'name':'prithvi','roll':1,'city':'mumbai'}

# json_data = json.dumps(data)
# r = requests.post(url=URL, data = json_data)

# data = r.json()

# print(data)

import requests
import json

# Use the correct endpoint (decide if you want /api/ or /api/api/)
URL = "http://127.0.0.1:8000/api/api/"   # if you removed extra 'api/' from app urls

data = {'name': 'prithvi', 'roll': 1, 'city': 'mumbai'}

# Send JSON with correct headers
r = requests.post(url=URL, data=json.dumps(data), headers={"Content-Type": "application/json"})

print("Status Code:", r.status_code)
print("Response Text:", r.text)

try:
    data = r.json()
    print("Parsed JSON:", data)
except Exception as e:
    print("Not JSON:", e)
