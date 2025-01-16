import requests
from datetime import datetime

USERNAME = "san-vin-git"
TOKEN = "iausabdcbyybxc"
graph_id = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":graph_id,
    "name":"Coding Graph",
    "unit": "hours",
    "type":"float",
    "color":"momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

today = datetime.now()

pixel_keys = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "8",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
response = requests.post(url=pixel_endpoint,json=pixel_keys,headers=headers)
print(response.text)





