import requests
import datetime as dt

# formatting the date
date = dt.datetime.now()
year = str(date.year)
month = '{:02d}'.format(date.month)
day = '{:02d}'.format(date.day)

# consts
USER = "_YOUR_USER_"  # your input goes here
TOKEN = "_YOUR_TOKEN_"  # your input goes here
GRAPH_ID = "_YOUR_GRAPH_ID_"  # your input goes here
TODAY = year+month+day


headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Commit Graph",  # name of graph
    "unit": "commit",  # use documentation to choose unit type
    "type": "int",  # int or float
    "color": "momiji",  # change color here using documentation
}

pixel_add = {
    "date": TODAY,
    "quantity": "3",   # change this value as needed
}

# update parameters
pixel_update = {
    "quantity": "5",  # change this value as needed
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
pixel_add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint = f"{pixel_add_endpoint}/{TODAY}"

# Create User
response = requests.post(url=pixela_endpoint, json=pixela_params)
print(response.text)

# Create Graph
# graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph.text)

# Add Pixel
# pixel = requests.post(url=pixel_add_endpoint, json=pixel_add, headers=headers)
# print(pixel.text)

# Update Pixel
# update = requests.put(url=update_endpoint, json=pixel_update, headers=headers)
# print(update.text)

# Delete Pixel
# clear_pixel = requests.delete(url=update_endpoint, headers=headers)
# print(clear_pixel.text)

