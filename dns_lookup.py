import socket
import time

uri = "www.naver.com"
start = time.time()
host = socket.gethostbyname(uri)
end = time.time()
diff = end - start
print 'host:', host
print str(diff) + '(s)'

info = socket.getaddrinfo(uri, 80)
print info
