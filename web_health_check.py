import requests
import socket
from pprint import pformat
import time


def avg_check(url):
    count = 5
    total_elapsed = 0
    for idx in xrange(count):
        res = requests.get(url)
        total_elapsed += res.elapsed.total_seconds()

    elapsed_time = total_elapsed / count
    # print 'elapsed time:', elapsed_time

    return elapsed_time


def dns_lookup(host):
    """DNS Lookup
    :param host - hostname
    """
    start = time.time()
    ip = socket.gethostbyname(host)
    end = time.time()
    print 'ip:', ip
    print 'lookup_time:', end - start

    start = time.time()
    host_info = socket.getaddrinfo(host, 80)
    end = time.time()
    print 'host_info:', pformat(host_info)
    print 'lookup_time:', end - start


def check_urls(url_list):
    # print 'url_list:', url_list

    f = open(url_list)
    for url in f.readlines():
        ttfb = avg_check(url)
        print '%-40s :' % url.strip(), '%f(s)' % ttfb




def main():
    url = 'http://comic.naver.com'
    # avg_check(url)

    host = 'comic.naver.com'
    # dns_lookup(host)

    url_list = './url_list.txt'
    check_urls(url_list)


if __name__ == '__main__':
    main()
