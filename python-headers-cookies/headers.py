import requests
 
session = requests.Session()
response = session.get('http://www.example.com')
headers = response.headers
session.close()
 
for header in headers:
    print(header + "\t" + headers[header])