import httplib
import urllib
import urllib2
import requests
import time


def use_httplib():
    """Use httplib module
    refer : https://docs.python.org/2/library/httplib.html
    """
    print '#' * 30
    print '# Use httplib #'

    try:
        start = time.time()
        print 'start:', start

        conn = httplib.HTTPConnection('www.stackoverflow.com')
        conn.request('GET', '/')  # GET, HEAD, POST, ....

        # Should be called after a request is sent to get the response from the server.
        # Returns an HTTPResponse instance.
        res = conn.getresponse()

        # netstat -napc | grep :80
        conn.close()  # Close the connection to the server

        data = res.read()
        print 'data:', data

        end = time.time()
        print 'end:', end

        elapsed_time = end - start
        print 'elapsed_time:', elapsed_time

        print res.status, ':', res.reason

    except Exception as e:
        print 'Error:', e

    print '#' * 30 + '\n\n'


def use_urllib():
    """Use urllib module
    refer : https://docs.python.org/2/library/urllib.html
    """
    print '#' * 30
    print '# Use urllib #'

    try:
        start = time.time()
        print 'start:', start

        res = urllib.urlopen('http://www.stackoverflow.com')
        end = time.time()
        print 'end:', end

        print dir(res)
        print 'info:', res.info()
        print 'headers:', res.headers
        print 'geturl:', res.geturl()
        print 'code:', res.getcode()
        # print 'data:', res.read()  #

        res.close()

        elapsed_time = end - start
        print 'elapsed_time:', elapsed_time

    except Exception as e:
        print 'Error:', e

    print '#' * 30 + '\n\n'


def use_urllib2():
    """Use urllib2 module
    refer : https://docs.python.org/2/library/urllib2.html
    """
    print '#' * 30
    print '# Use urllib2 #'

    try:
        start = time.time()
        print 'start:', start

        url = 'http://www.stackoverflow.com'
        values = {'name': 'Michael Foord',
                  'location': 'Northampton',
                  'language': 'Python'}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        req.add_header('Referer', 'http://www.python.org/')     # can assemble header

        # Open the URL url, which can be either a string or a Request object.
        # res = urllib2.urlopen(url, data)
        res = urllib2.urlopen(req)

        end = time.time()
        print 'end:', end

        print dir(res)
        print 'info:', res.info()
        print 'headers:', res.headers
        print 'geturl:', res.geturl()
        print 'code:', res.getcode()
        print 'msg:', res.msg   # add msg in urllib2
        # print 'data:', res.read()  #

        res.close()

        elapsed_time = end - start
        print 'elapsed_time:', elapsed_time

    except Exception as e:
        print 'Error:', e

    print '#' * 30 + '\n\n'


def use_requests():
    """Use requests module
    refer : http://docs.python-requests.org/
    """
    print '#' * 30
    print '# Use requests #'

    try:
        start = time.time()
        print 'start:', start

        #username = ''
        #password = ''
        #res = requests.get('https://api.github.com/user', auth=(username, password))
        res = requests.get('http://www.stackoverflow.com')
        end = time.time()
        print 'end:', end

        print 'res:', dir(res)

        print 'content-type:', res.headers['content-type']
        print 'headers:', res.headers
        print 'encoding:', res.encoding
        print 'text:', res.text
        print 'status code:', res.status_code
        print 'reason:', res.reason
        print 'elapsed:', res.elapsed
        """ http://docs.python-requests.org/en/latest/api/?highlight=elapsed#requests.Response.elapsed
        The amount of time elapsed between sending the request and the arrival of the response (as a timedelta).
        This property specifically measures the time taken between sending the first byte of the request and finishing
        parsing the headers. It is therefore unaffected by consuming the response content or the value of the stream
        keyword argument.
        """
        #print 'elapsed:', dir(res.elapsed)
        #print 'elapsed:', res.elapsed.seconds
        print 'elapsed:', res.elapsed.total_seconds()

        elapsed_time = end - start
        print 'elapsed_time:', elapsed_time

    except Exception as e:
        print 'Error:', e

    print '#' * 30 + '\n\n'


def main():
    use_httplib()
    use_urllib()
    use_urllib2()
    use_requests()


if __name__ == '__main__':
    main()
