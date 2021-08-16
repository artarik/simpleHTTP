#!/usr/bin/env python3
import urllib.request

openstream = urllib.request.urlopen("http://localhost:1234")
encContent = openstream.read()
decContent = encContent.decode("utf8")
print(decContent)
openstream.close()

