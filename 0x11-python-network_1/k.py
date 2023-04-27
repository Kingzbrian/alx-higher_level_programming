#!/usr/bin/python3
#fetching a urlusing urllib
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as responce:
    html = responce.read
