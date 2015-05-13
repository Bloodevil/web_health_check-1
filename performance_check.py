""" Time To First Byte (http://en.wikipedia.org/wiki/Time_To_First_Byte)
Time To First Byte or TTFB is a measurement that is often used as an indication of the responsiveness of a webserver or other network resources.

It is the duration from the virtual user making an HTTP request to the first byte of the page being received by the browser. This time is made up of the socket connection time, the time taken to send the HTTP request, and the time taken to get the first byte of the page.
"""

import requests
from bs4 import BeautifulSoup
import time
import socket

start_time = time.time()
total_time = 0


def dns_lookup(host):
    start = time.time()
    ip = socket.gethostbyname(host)
    end = time.time()

    return end - start


def main():
    url = 'http://comic.naver.com/webtoon/detail.nhn?titleId=644180&no=134&weekday=tue'
    res = requests.get(url)
    content = res.content
    #print 'content:', content

    soup = BeautifulSoup(content)
    #print soup.prettify()
    for img in soup.find_all('img'):
        print img['src']




if __name__ == '__main__':
    main()
