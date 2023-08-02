#!/usr/bin/python3
from urllib import request
if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        content = res.read()
        print("Body responce:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))

