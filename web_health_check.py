import requests
import socket
from pprint import pformat
import time

def avg_check(url):
    count = 10
    total_elapsed = 0
    for idx in xrange(count):
        res = requests.get(url)
        total_elapsed += res.elapsed.total_seconds()
    print 'elapsed time:', total_elapsed / count


def dns_lookup(host):
    """DNS Lookup
    :param host - hostname
    """

    ip = socket.gethostbyname(host)
    print 'ip:', ip

    host_info = socket.getaddrinfo(host, 80)
    print 'host_info:', pformat(host_info)



def main():
    url = 'http://comic.naver.com'
    # avg_check(url)

    host = 'comic.naver.com'
    start = time.time()
    dns_lookup(host)
    end = time.time()
    lookup_time = end - start

    print 'start:', start
    print 'end:', end
    print 'lookup_time:', lookup_time

if __name__ == '__main__':
    main()
