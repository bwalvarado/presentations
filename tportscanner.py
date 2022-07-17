import sys
import socket
import threading
from queue import Queue
 
socket.setdefaulttimeout(0.25)
 
q = Queue()
 
def scanner(host, port):
    ip = socket.gethostbyname(host)
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
 
def worker():
    while True:
        target = q.get()
        scanner(target[0], target[1])
        q.task_done()
 
def main():
    if len(sys.argv) == 1:
        print("Missing host")
    else:
        host = sys.argv[1]
 
        for w in range(100):
            threading.Thread(target=worker, daemon=True).start()
 
        for port in range(65535):
            q.put((host, port))
 
        q.join()
 
if __name__ == '__main__':
    main()