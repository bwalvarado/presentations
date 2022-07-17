import requests
 
session = requests.Session()
response = session.get('https://www.github.com')
cookies = response.cookies.get_dict()
 
for c in cookies:
    print (c + " : " + cookies[c])