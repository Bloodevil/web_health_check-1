import socket
import time


start = time.time()
host = socket.gethostbyname('www.daum.net')
end = time.time()
diff = end - start
print 'host:', host
print str(diff) + '(s)'


info = socket.getaddrinfo("www.daum.net", 80)
print info
