import requests

response = requests.get('http://localhost:8000/')
print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)