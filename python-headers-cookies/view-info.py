import sys
import requests
 
def view_info(url):
    session = requests.Session()
    response = session.get(url)
    cookies = response.cookies.get_dict()
    headers = response.headers
    
    print("\nCookies\n")
    for c in cookies:
        print (c + " : " + cookies[c])
 
    print("\nHEADERS\n")
    for h in headers:
        print(h + " : " + headers[h])
    
def main():
	if len(sys.argv) == 1:
		print("Missing URL")
	else:
		view_info(sys.argv[1])
		
if __name__ == '__main__':
	main()