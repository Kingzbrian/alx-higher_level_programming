#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as responce:
    html = responce.read

