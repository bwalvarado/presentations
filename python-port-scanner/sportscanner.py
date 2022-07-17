import socket

socket.setdefaulttimeout(0.25)
ip = socket.gethostbyname('scanme.nmap.org')

for port in range(65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex((ip, port))
	if result == 0:
		print('Port {}: OPEN'.format(port))
	s.close()