#!/usr/bin/python3
"""Take in a URL, send request to URL and display value of `X-Request-Id`"""
import sys
from urllib import request

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1],  data)
    with request.urlopen(req) as res:
        print(res.read.decode("utf-8"))

