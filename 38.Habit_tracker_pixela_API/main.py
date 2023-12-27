import requests
import os
from datetime import datetime

# To create a user
PIXEL_USERNAME = os.environ.get("PIXEL_USERNAME")
PIXEL_TOKEN = os.environ.get("PIXEL_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "mygraph1"
GRAPH_NAME = "Cycling Graph"

user_params = {
    "token": PIXEL_TOKEN,
    "username": PIXEL_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# To create a graph
graph_endpoint = f"{pixela_endpoint}/{PIXEL_USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "km",
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": PIXEL_TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# To post a pixel
today = datetime.now()
date = today.strftime("%Y%m%d")
mygraph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_graph_config = {
    "date": date,
    "quantity": input("How many km did you cycled today? "),
}
response = requests.post(url=mygraph_endpoint, json=post_graph_config, headers=headers)
print(response.text)

# To update a pixel
mypixel_endpoint = f"{mygraph_endpoint}/{date}"
mypixel_config = {
    "quantity": "2.0"
}
# response = requests.put(url=mypixel_endpoint, json=mypixel_config, headers=headers)
# print(response.text)

# To delete a pixel
# response = requests.delete(url=mypixel_endpoint, headers=headers)
# print(response.text)
