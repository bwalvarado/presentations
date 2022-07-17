import requests
session = requests.Session()
response = session.get("http://www.example.com")
print(response)
print(response.status_code)
print(response.reason)
print(response.content)
print(response.text)
print(response.headers)