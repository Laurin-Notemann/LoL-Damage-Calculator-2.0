import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE + "data")
print(response.json())
