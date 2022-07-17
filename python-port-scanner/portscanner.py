import sys
import socket

socket.setdefaulttimeout(0.25)

def scanner(host):
	ip = socket.gethostbyname(host)
	for port in range(65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			result = s.connect_ex((ip, port))
			if result == 0:
				print('Port {}: OPEN'.format(port))
			s.close()
		except socket.error:
			print('Connection error')
			sys.exit()
		except KeyboardInterrupt:
			sys.exit()

def main():
	if len(sys.argv) == 1:
		print("Missing host")
	else:
		scanner(sys.argv[1])
		
if __name__ == '__main__':
	main()