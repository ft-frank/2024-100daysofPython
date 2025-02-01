import requests

token = "sfjsdflksklsjlsls"
username =  "frankenstein"
pixela_endpoint = "https://pixe.la/v1/users"

#CREATING ACCOUNTS
user_params = {
    "token": "sfjsdflksklsjlsls",
    "username": "frankenstein",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

#CREATING GRAPHS
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Studying Graph",
    "unit": "min",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token



}

# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)

#ADDING PIXELS

data = {
    "date": "20240311",
    "quantity": "51"



}


response = requests.post(url = "https://pixe.la/v1/users/frankenstein/graphs/graph2", headers = headers, json = data)
print(response.raise_for_status())