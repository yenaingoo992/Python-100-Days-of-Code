import requests
from datetime import datetime

USER_NAME = "yenaing"
TOKEN = "mbnx25wchyd2v5rh2235sc"
GRAPH_ID = "graph01"

endpoints = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user creation
# response = requests.post(url=endpoints, json=user_params)
# print(response.text)

graph_endpoints = f"{endpoints}/{USER_NAME}/graphs"

graph_configs = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create graph
# graph_response = requests.post(url=graph_endpoints, json=graph_configs, headers=headers)
# print(graph_response.text)

post_pixel_endpoints = f"{graph_endpoints}/{GRAPH_ID}"

today = datetime.now()
str_today = today.strftime("%Y%m%d")

pixel_configs = {
    "date": str_today,
    "quantity": "2"
}

# create pixel
pixel_response = requests.post(url=post_pixel_endpoints, json=pixel_configs, headers=headers)
print(pixel_response.text)

update_pixel_endpoints = f"{graph_endpoints}/{GRAPH_ID}/{str_today}"

update_configs = {
    "quantity": "4"
}

# update pixel
# update_response = requests.put(url=update_pixel_endpoints, json=update_configs, headers=headers)
# print(update_response.text)

delete_pixel_endpoints = f"{graph_endpoints}/{GRAPH_ID}/{str_today}"
# delete pixel
# delete_response = requests.delete(url=delete_pixel_endpoints, headers=headers)
# print(delete_response.text)