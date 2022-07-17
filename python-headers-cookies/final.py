import sys
import requests

def check(url):
    session = requests.Session()
    response = session.get(url)
    headers = response.headers
    csp = response.headers['Content-Security-Policy']
 
    x_xss_protection = False
    x_frame_options = False
    x_content_type_options = False
    strict_transport_security = False
    x_permitted_cross_domain_policies = False
    content_security_policy = False

    print("Checking for presence of required security headers...")
    for header in headers:
        if header.upper() == "X-XSS-PROTECTION":
            x_xss_protection = True
        elif header.upper() == "X-FRAME-OPTIONS":
            x_frame_options = True
        elif header.upper() == "X-CONTENT-TYPE-OPTIONS":
            x_content_type_options = True
        elif header.upper() == "STRICT-TRANSPORT-SECURITY":
            strict_transport_security = True
        elif header.upper() == "X-PERMITTED-CROSS-DOMAIN-POLICIES":
            x_permitted_cross_domain_policies = True
        elif header.upper() == "CONTENT-SECURITY-POLICY":
            content_security_policy = True
        else:
            pass
 
    if x_xss_protection == False:
        print("X-XSS-Protection missing")
    if x_frame_options == False:
        print("X-Frame-Options missing")
    if x_content_type_options == False:
        print("X-Content-Type-Options missing")
    if strict_transport_security == False:
        print("Strict-Transport-Security missing")
    if x_permitted_cross_domain_policies == False:
        print("X-Permitted-Cross-Domain-Policies missing")
    if content_security_policy == False:
        print("Content-Security-Policy missing")
    
    print("Checking for unsafe csp entries...")
    for c in csp.split():
        if "unsafe" in c:
            print(c)
        
def main():
	if len(sys.argv) == 1:
		print("Missing URL")
	else:
		check(sys.argv[1])
		
if __name__ == '__main__':
	main()